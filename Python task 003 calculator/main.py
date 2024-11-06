import math

def calculator():
    print("Welcome to the Advanced Python Calculator!")
    
    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation (x^y)")
        print("6. Square Root (√x)")
        print("7. Quit")
        
        choice = input("What would you like to do? (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Thanks for using the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                if choice == '6':
                    num1 = float(input("Enter the number: "))
                    if num1 < 0:
                        print("Sorry, you can't take the square root of a negative number in the real number system.")
                        continue
                    result = math.sqrt(num1)
                    print(f"√{num1} = {result}")
                    continue
                else:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Oops! Please enter valid numerical values.")
                continue
            
            if choice == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Sorry, you can't divide by zero.")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                result = num1 ** num2
                print(f"{num1} ^ {num2} = {result}")
            
        else:
            print("Hmm, that wasn't a valid choice. Please choose a number between 1 and 7.")
        
        again = input("\nWould you like to do another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Okay, take care and have a great day!")
            break

if __name__ == "__main__":
    calculator()
