from flask import Flask, render_template, request, redirect, url_for, flash
from models import init_db, add_expense, get_expenses, delete_expense, get_summary
from utils import check_budget, get_budget, set_budget

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    expenses = get_expenses()
    summary = get_summary()
    alert = check_budget(summary['total'])
    return render_template('index.html', expenses=expenses, summary=summary, alert=alert, budget=get_budget())

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])
        category = request.form['category']
        note = request.form['note']
        add_expense(date, amount, category, note)
        flash('Expense added successfully!')
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/delete/<int:expense_id>')
def delete(expense_id):
    delete_expense(expense_id)
    flash('Expense deleted successfully!')
    return redirect(url_for('index'))

@app.route('/set_budget', methods=['POST'])
def budget():
    amount = float(request.form['budget'])
    set_budget(amount)
    flash('Monthly budget updated!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
