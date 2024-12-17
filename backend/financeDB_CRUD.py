import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ayan6100.",
    database = "finance"
)

cursor = connection.cursor()


def add_income(amount, category, date, description):
    query = "INSERT INTO income (incomeAmount, incomeCategory, incomeDate, incomeDescription) VALUES (%s, %s, %s, %s)"
    values = (amount, category, date, description)
    cursor.execute(query, values)
    connection.commit()

def get_incomes():
    query = "SELECT * FROM income"
    cursor.execute(query)
    return cursor.fetchall()

def update_income(income_id, amount, category, date, description):
    query = "UPDATE income SET incomeAmount = %s, incomeCategory = %s, incomeDate = %s, incomeDescription = %s WHERE incomeID = %s"
    values = (amount, category, date, description, income_id)
    cursor.execute(query, values)
    connection.commit()

def delete_income(income_id):
    query = "DELETE FROM income WHERE incomeID = %s"
    cursor.execute(query, (income_id,))
    connection.commit()

def add_expense(amount, category, date, description):
    query = "INSERT INTO expenses (expenseAmount, expenseCategory, expenseDate, expenseDescription) VALUES (%s, %s, %s, %s)"
    values = (amount, category, date, description)
    cursor.execute(query, values)
    connection.commit()

def get_expenses():
    query = "SELECT * FROM expenses"
    cursor.execute(query)
    return cursor.fetchall()

def update_expense(expense_id, amount, category, date, description):
    query = "UPDATE expenses SET expenseAmount = %s, expenseCategory = %s, expenseDate = %s, expenseDescription = %s WHERE expenseID = %s"
    values = (amount, category, date, description, expense_id)
    cursor.execute(query, values)
    connection.commit()

def delete_expense(expense_id):
    query = "DELETE FROM expenses WHERE expenseID = %s"
    cursor.execute(query, (expense_id,))
    connection.commit()