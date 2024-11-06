import datetime

class Transaction:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.date.today()

    def __str__(self):
        return f"{self.date} - {self.category}: ${self.amount:.2f}"

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category):
        if amount == 0:
            print("Amount can't be zero.")
            return
        transaction = Transaction(amount, category)
        self.transactions.append(transaction)
        print(f"Transaction added: {transaction}")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded yet.")
            return
        print("\nYour Transactions:")
        for transaction in self.transactions:
            print(transaction)

    def view_summary(self):
        if not self.transactions:
            print("No transactions to summarize.")
            return
        total_income = sum(t.amount for t in self.transactions if t.amount > 0)
        total_expense = sum(t.amount for t in self.transactions if t.amount < 0)
        balance = total_income + total_expense
        print("\nFinancial Summary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${abs(total_expense):.2f}")
        print(f"Current Balance: ${balance:.2f}")

    def start(self):
        print("Welcome to your Personal Finance Tracker!")
        while True:
            print("\nChoose an option:")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Transactions")
            print("4. View Summary")
            print("5. Exit")
            choice = input("What would you like to do? (1/2/3/4/5): ")

            if choice == '1':
                amount = float(input("Enter income amount: $"))
                category = input("Enter income category (e.g., Salary, Gift): ")
                self.add_transaction(amount, category)
            elif choice == '2':
                amount = float(input("Enter expense amount: $"))
                category = input("Enter expense category (e.g., Rent, Groceries): ")
                self.add_transaction(-amount, category)
            elif choice == '3':
                self.view_transactions()
            elif choice == '4':
                self.view_summary()
            elif choice == '5':
                print("Thank you for using the Personal Finance Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = FinanceTracker()
    tracker.start()
