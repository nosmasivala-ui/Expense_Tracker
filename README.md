# 💰 Smart Expense Tracker Application

A premium, production-ready personal finance tracker web application built with **Django** and **SQLite**. This application features a fully responsive, modern dashboard interface designed from scratch using **Tailwind CSS**, allowing users to manage transactions, categorize expenditures, and review real-time monthly financial metrics.

---

## 🛠️ Tech Stack & Development Tools

- **Backend Architecture:** Python 3.14+ & Django 6.0+ (Model-View-Template pattern)
- **Database Engine:** SQLite (Native relational database configuration)
- **Frontend Framework:** Tailwind CSS 4.0 (Utility-first fluid layout design framework)
- **Typography:** Google Fonts (`Plus Jakarta Sans` typography profile)
- **Version Control:** Git & GitHub

---

## 🚀 Application Core Features

Every functional requirement for an enterprise-level financial logger is fully implemented directly on the server side:

### 1. Full Transaction CRUD Management
- **Add Expenses:** Log title, precise amount, date, description, and custom category tags.
- **Edit/Update Records:** Seamlessly update transaction parameters using pre-populated reactive forms.
- **Delete Records:** Safe execution pattern to completely erase ledger entries with confirmation safeguards.

### 2. Search Engine & Filtering
- **Keyword Search:** Instant server-side filter tracking for specific item names (e.g., looking up "Lunch" or "Clothes").
- **Category Filter:** Dropdown filtering to isolate specific areas of expenditure instantly.

### 3. Live Metrics & Analytics Reporting
- **Category Summary Sidebar:** Dynamically aggregates totals per category on the main dashboard screen.
- **Monthly Expenditure Report:** A dedicated premium dashboard view tracking real-time total monthly expenditure and localized currency breakdowns.
- **Rupee Localization (₹):** Complete interface adjustment displaying all ledger statements in Indian Rupees.

---

## 💾 Relational Database Schema Design

The application profile leverages two principal data tables mapped via clean Object-Relational Mapping (ORM) and relational integrity rules:

### I. Category Schema (`Category` Model)
Used to scope distinct spending sectors cleanly.
- `name` (`CharField`, max_length=50): Unique lookup category titles.

### II. Expense Schema (`Expense` Model)
The main data ledger table structured with database constraint safety.
- `title` (`CharField`, max_length=100): Transaction descriptor item.
- `amount` (`DecimalField`, max_digits=10, decimal_places=2): High-precision financial scale mapping.
- `category` (`ForeignKey`): Relational bridge pointing to `Category`. Configured with `on_delete=models.SET_NULL, null=True` so that erasing a category doesn't delete your transaction records.
- `date` (`DateField`): Defaults automatically to the entry timestamp.
- `description` (`TextField`): Paragraph field allowing secondary entry details.

---

## 💻 Technical Skills Applied

- **Object-Oriented Programming (OOP):** Implementing explicit encapsulation overrides inside model structures (`__str__` initialization hooks).
- **Advanced Query Optimization:** Utilizing Django DB aggregation tools (`Sum`, `values`, `annotate`) to execute heavy summary calculations on the database runtime rather than slowing down the frontend.
- **Exception Handling & Validation:** Built-in validation loops wrapped in clean server-side `try-except` statements to catch incomplete form submissions gracefully.

---

