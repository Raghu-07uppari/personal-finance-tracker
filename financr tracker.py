import datetime

class FinanceTracker:
    def __init__(self):
        self.monthly_budget = 0.0
        self.incomes = []
        self.expenses = []

    def set_budget(self, budget):
        if budget <= 0:
            print("Budget must be positive and non zero.")
            return
        self.monthly_budget = budget
        print(f"Monthly budget set to ${budget:.2f}")

    def add_income(self, amount, description, date=None):
        if amount <= 0:
            print("Income must be positive and non-zero.")
            return
        if date is None:
            date = datetime.date.today()
        elif isinstance(date, str):
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
        self.incomes.append({'amount': amount, 'description': description, 'date': date})
        print(f"Income added: ${amount:.2f} - {description} on {date}")

    def add_expense(self, amount, description, date=None):
        if amount <= 0:
            print("Expense must be positive and non-zero.")
            return
        if date is None:
            date = datetime.date.today()
        elif isinstance(date, str):
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
        self.expenses.append({'amount': amount, 'description': description, 'date': date})
        print(f"Expense added: ${amount:.2f} - {description} on {date}")

    def view_incomes(self):
        if not self.incomes:
            print("No incomes recorded.")
            return
        print("All Incomes:")
        for i, income in enumerate(self.incomes, 1):
            print(f"{i}. ${income['amount']:.2f} - {income['description']} on {income['date']}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("All Expenses:")
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i}. ${expense['amount']:.2f} - {expense['description']} on {expense['date']}")

    def monthly_summary(self, year=None, month=None):
        if year is None or month is None:
            # Default to current month
            now = datetime.date.today()
            year = now.year
            month = now.month
        else:
            try:
                year = int(year)
                month = int(month)
                if not (1 <= month <= 12):
                    print("Invalid month. Must be between 1 and 12.")
                    return
            except ValueError:
                print("Invalid year or month.")
                return

        filtered_incomes = [i for i in self.incomes if i['date'].year == year and i['date'].month == month]
        filtered_expenses = [e for e in self.expenses if e['date'].year == year and e['date'].month == month]

        total_income = sum(income['amount'] for income in filtered_incomes)
        total_expenses = sum(expense['amount'] for expense in filtered_expenses)
        remaining_budget = self.monthly_budget - total_expenses
        print(f"Monthly Summary for {year}-{month:02d}:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")
        if remaining_budget < 0:
            print("Warning: You have exceeded your budget!")

def main():
    tracker = FinanceTracker()
    while True:
        print("\nPersonal Finance Tracker Menu:")
        print("1. Set Monthly Budget")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. View All Incomes")
        print("5. View All Expenses")
        print("6. Monthly Summary")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            try:
                budget = float(input("Enter monthly budget: "))
                tracker.set_budget(budget)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            try:
                amount = float(input("Enter income amount: "))
                description = input("Enter income description: ").strip()
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                date = date_input if date_input else None
                tracker.add_income(amount, description, date)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '3':
            try:
                amount = float(input("Enter expense amount: "))
                description = input("Enter expense description: ").strip()
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                date = date_input if date_input else None
                tracker.add_expense(amount, description, date)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '4':
            tracker.view_incomes()
        elif choice == '5':
            tracker.view_expenses()
        elif choice == '6':
            year_input = input("Enter year (e.g., 2023) or press Enter for current year: ").strip()
            month_input = input("Enter month (1-12) or press Enter for current month: ").strip()
            year = int(year_input) if year_input else None
            month = int(month_input) if month_input else None
            tracker.monthly_summary(year, month)
        elif choice == '7':
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()