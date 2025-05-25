import json
import os

BUDGET_FILE = 'budget.json'

def get_budget():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, 'r') as f:
            return json.load(f).get('monthly_budget', 0)
    return 0

def set_budget(amount):
    with open(BUDGET_FILE, 'w') as f:
        json.dump({'monthly_budget': amount}, f)

def check_budget(current_total):
    budget = get_budget()
    if budget and current_total > budget:
        return f"Alert: You have exceeded your monthly budget of ₹{budget}!"
    return None
