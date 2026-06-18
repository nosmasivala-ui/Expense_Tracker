\# 💰 Smart Expense Tracker



A modern, responsive web application built with \*\*Django\*\* and \*\*SQLite\*\* to log, track, and analyze personal financial expenditures. This project applies Object-Oriented Programming (OOP) design, custom relational database schema modeling, and clean server-side data processing wrapped in a premium, modern interface.



\## 🚀 Features



\- \*\*Full CRUD Management:\*\* Easily add, display, edit, and delete transactions.

\- \*\*Advanced Server-Side Filtering:\*\* Real-time lookup search engine for keywords and targeted dropdown category filtering.

\- \*\*Live Category Summaries:\*\* Dynamic financial analysis panels prepared dynamically on the server side.

\- \*\*Monthly Expenditure Breakdown:\*\* Dedicated reporting view with automated local currency calculations showing total monthly tracking.

\- \*\*Premium Interface Design:\*\* Built entirely using utility-first fluid classes from Tailwind CSS and typeset in Plus Jakarta Sans.



\---



\## 🛠️ Tech Stack \& Skills Covered



\- \*\*Backend Framework:\*\* Django (Python)

\- \*\*Database Engine:\*\* SQLite

\- \*\*Architecture:\*\* Model-View-Template (MVT)

\- \*\*Frontend Engine:\*\* Tailwind CSS via asynchronous CDN runtime injection

\- \*\*Core Engineering Principles:\*\* - Object-Oriented Programming (OOP)

&#x20; - Custom Relational Schema Mapping

&#x20; - Query Optimization via Database Aggregation (`Sum`, `values`, `annotate`)

&#x20; - Server-side Exception/Error Validation



\---



\## 💾 Relational Database Schema Design



The backend storage profile utilizes two primary models linked natively via database constraints:



\### 1. Category Model

Stores specific categorization scopes (e.g., Food, Utilities, Entertainment, Rent).

\- `name`: Unique character array configuration (`max\_length=50`)



\### 2. Expense Model

Tracks distinct transactional items tied dynamically to categories via a Foreign Key structural boundary.

\- `title`: Character string input descriptor (`max\_length=100`)

\- `amount`: Multi-digit decimal layout field (`max\_digits=10`, `decimal\_places=2`)

\- `category`: Relational Foreign Key field linked to `Category` (`on\_delete=models.SET\_NULL, null=True`)

\- `date`: System timezone tracking date picker default array configuration

\- `description`: Optional text paragraph data canvas (`blank=True, null=True`)



\---



\## 💻 Installation \& Local Activation Blueprint



Follow these procedures to launch the tracking core locally on a Windows platform:



\### 1. Clone \& Access the Repository

```bash

git clone \[https://github.com/nosmasivala-ui/Expense\_Tracker.git](https://github.com/nosmasivala-ui/Expense\_Tracker.git)

cd Expense\_Tracker

