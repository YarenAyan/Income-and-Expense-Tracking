from backend.financeDB_CRUD import add_income, get_incomes, update_income, delete_income

# Test 1: Create
print("Adding income...")
add_income(2000, "Part-time Job", "2024-12-15", "Salary for part-time work")
print("Income added.")

# Test 2: Read
print("Fetching all incomes...")
incomes = get_incomes()
for income in incomes:
    print(income)

# Test 3: Update
print("Updating income...")
update_income(1, 2500, "Updated Salary for part-time job")
print("Income updated.")

# Test 4: Delete
print("Deleting income...")
delete_income(1)
print("Income deleted.")