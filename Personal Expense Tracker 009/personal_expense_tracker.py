

def add_expense():
    date = input("Enter the date (DD/MM/YYYY): ")
    category = input("Enter the expense category (e.g., Food, Transport): ")
    amount = float(input("Enter the amount: "))
    
   
    with open('expenses.txt', 'a') as file:
        file.write(f"{date},{category},{amount}\n")
    print("Expense added successfully!\n")

def view_expenses():
    try:
        with open('expenses.txt', 'r') as file:
            print("\nYour Expenses:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No expense records found.\n")

def delete_expense():
    try:
        with open('expenses.txt', 'r') as file:
            lines = file.readlines()
        
        if len(lines) == 0:
            print("No expenses to delete.\n")
            return
        
        print("Select the expense number to delete:")
        for idx, line in enumerate(lines, start=1):
            print(f"{idx}. {line.strip()}")
        
        expense_num = int(input("Enter the expense number to delete: "))
        
        if 1 <= expense_num <= len(lines):
            lines.pop(expense_num - 1)
            with open('expenses.txt', 'w') as file:
                file.writelines(lines)
            print("Expense deleted successfully!\n")
        else:
            print("Invalid expense number.\n")
    except FileNotFoundError:
        print("No expense records found.\n")

def main():
    while True:
        print("Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
