# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from .models import Expense, Category
from datetime import datetime

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    
    # Filter/Search implementation
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    
    if search_query:
        expenses = expenses.filter(title__icontains=search_query)
    if category_filter:
        expenses = expenses.filter(category__id=category_filter)
        
    categories = Category.objects.all()
    
    # Calculate Category Totals safely on the server side
    category_totals_raw = Expense.objects.values('category__name').annotate(total=Sum('amount'))
    
    # Process categories safely into a clean format to prevent HTML parsing errors
    processed_totals = []
    for item in category_totals_raw:
        name = item['category__name'] if item['category__name'] else "Uncategorized"
        processed_totals.append({
            'name': name,
            'total': item['total']
        })

    context = {
        'expenses': expenses,
        'categories': categories,
        'category_totals': processed_totals,  # Clean, plain Python list
    }
    return render(request, 'expenses/expense_list.html', context)

def add_expense(request):
    if request.method == "POST":
        try:
            title = request.POST.get('title')
            amount = request.POST.get('amount')
            category_id = request.POST.get('category')
            date = request.POST.get('date')
            description = request.POST.get('description')

            if not title or not amount:
                raise ValueError("Required fields are missing.")

            category = Category.objects.get(id=category_id) if category_id else None
            
            Expense.objects.create(
                title=title,
                amount=amount,
                category=category,
                date=date if date else datetime.today().date(),
                description=description
            )
            messages.success(request, "Expense added successfully!")
            return redirect('expense_list')
        except Exception as e:
            messages.error(request, f"Error adding expense: {e}")
            
    categories = Category.objects.all()
    return render(request, 'expenses/expense_form.html', {'categories': categories})

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        try:
            expense.title = request.POST.get('title')
            expense.amount = request.POST.get('amount')
            category_id = request.POST.get('category')
            expense.category = Category.objects.get(id=category_id) if category_id else None
            if request.POST.get('date'):
                expense.date = request.POST.get('date')
            expense.description = request.POST.get('description')
            
            expense.save()
            messages.success(request, "Expense updated successfully!")
            return redirect('expense_list')
        except Exception as e:
            messages.error(request, f"Error updating expense: {e}")

    categories = Category.objects.all()
    return render(request, 'expenses/expense_form.html', {'expense': expense, 'categories': categories})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        expense.delete()
        messages.success(request, "Expense deleted successfully!")
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})

def monthly_report(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    monthly_expenses = Expense.objects.filter(date__month=current_month, date__year=current_year)
    total_spent = monthly_expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    category_breakdown_raw = monthly_expenses.values('category__name').annotate(total=Sum('amount'))
    
    processed_breakdown = []
    for item in category_breakdown_raw:
        name = item['category__name'] if item['category__name'] else "Uncategorized"
        processed_breakdown.append({
            'name': name,
            'total': item['total']
        })
    
    context = {
        'total_spent': total_spent,
        'category_breakdown': processed_breakdown,
        'month_name': datetime.now().strftime('%B %Y')
    }
    return render(request, 'expenses/monthly_report.html', context)