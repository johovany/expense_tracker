# all functions are used so imported whole file
import classes


def main():
    tracker = classes.ExpenseTracker()

    while True:
        # print menu options
        print("\nExpense Trakcer Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter your selection (1-5): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the descripiton: ")
            amount = float(input("Enter the amount: "))

            # list for pre-defined categories user can choose from
            expense_categories = ["Food", "Rent/Mortgage", "Fun", "Utilities", "Other"]

            # loop to ensure user selects a cateogry
            while True:
                print("Select a category: ")
                for i, category_name in enumerate(expense_categories):
                    print(f"{i + 1}. {category_name}")

                category = int(input("Enter a category number: ")) - 1

                if category in range(len(expense_categories)):
                    category = expense_categories[category]
                    break
                elif category not in range(len(expense_categories)):
                    print("Invalid Option. Try Again")

            # assigns user provided info to expense class and expense trakcer
            expense = classes.Expense(date, description, amount, category)
            tracker.add_expense(expense)
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Have a nice day!")
            break
        else:
            print("Invalid option. Please try again.")


main()
