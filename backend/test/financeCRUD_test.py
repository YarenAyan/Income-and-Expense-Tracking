import sys
sys.path.append("C:/Users/monster/Desktop/budget/backend")
from financeDB_CRUD import add_income, get_incomes, update_income, delete_income, add_expense, get_expenses, update_expense, delete_expense

# Test 1: Create income
print("Adding income...")
add_income(1000, "test", "2024-12-15", "income test")
print("Income added.")

# Test 2: Read income
print("Fetching all incomes...")
incomes = get_incomes()
for income in incomes:
    print(income)

# Test 3: Update income
print("Updating income...")
update_income(1, 1500, "update income test")
print("Income updated.")

# Test 4: Delete income
print("Deleting income...")
delete_income(1)
print("Income deleted.")

# Test 5: Create expense
print("Adding expense...")
add_expense(1000, "test", "2024-12-15", "expense test")
print("Expense added.")

# Test 6: Read expense
print("Fetching all expenses...")
expenses = get_expenses()
for expense in expenses:
    print(expenses)

# Test 7: Update expense
print("Updating expense...")
update_expense(1, 1500, "update expense test")
print("Expense updated.")

# Test 8: Delete expense
print("Deleting expense...")
delete_expense(1)
print("Expense deleted.")