# initial expense class
class Expense:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category
        
# list to store expenses and functions to store tracker functionality
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    # function to add expenses
    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense Successfully Added")

    # function to remove expenses
    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense successfully deleted")
        else:
            print("Invalid expense selection")

    # function to view expenses
    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(
                    f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}, Category: {expense.category}"
                )

    # function to get sum of all expenses
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")
