import csv
from collections import defaultdict

def init_db():
    try:
        with open('expenses.csv', 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'date', 'amount', 'category', 'note'])
    except FileExistsError:
        pass

def add_expense(date, amount, category, note):
    expenses = get_expenses()
    new_id = expenses[-1][0] + 1 if expenses else 1
    with open('expenses.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([new_id, date, amount, category, note])

def get_expenses():
    try:
        with open('expenses.csv', newline='') as f:
            reader = csv.reader(f)
            next(reader)
            return [[int(row[0]), row[1], float(row[2]), row[3], row[4]] for row in reader]
    except FileNotFoundError:
        return []

def delete_expense(expense_id):
    expenses = get_expenses()
    expenses = [exp for exp in expenses if exp[0] != expense_id]
    with open('expenses.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'date', 'amount', 'category', 'note'])
        writer.writerows(expenses)

def get_summary():
    expenses = get_expenses()
    total = sum(exp[2] for exp in expenses)
    category_totals = defaultdict(float)
    for exp in expenses:
        category_totals[exp[3]] += exp[2]
    return {
        'total': total,
        'by_category': list(category_totals.items())
    }
