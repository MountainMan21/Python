import os

FILE_NAME = "students.txt"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        file.write("ID,Name,Age,Grade\n")

def display_students():
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        if len(lines) <= 1:
            print("No students available.")
            return
        for line in lines[1:]:
            print(line.strip())

def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{id},{name},{age},{grade}\n")
    print(f"Student {name} added successfully.")

def search_student():
    search_name = input("Enter student name to search: ")
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        found = False
        for line in lines[1:]:
            if search_name.lower() in line.split(',')[1].lower():
                print(line.strip())
                found = True
        if not found:
            print("Student not found.")

def update_student():
    id = input("Enter student ID to update: ")
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    updated = False
    with open(FILE_NAME, "w") as file:
        for line in lines:
            if line.startswith(id):
                name = input("Enter new student name: ")
                age = input("Enter new student age: ")
                grade = input("Enter new student grade: ")
                file.write(f"{id},{name},{age},{grade}\n")
                print(f"Student {id} updated successfully.")
                updated = True
            else:
                file.write(line)
    
    if not updated:
        print("Student ID not found.")

def delete_student():
    id = input("Enter student ID to delete: ")
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    deleted = False
    with open(FILE_NAME, "w") as file:
        for line in lines:
            if line.startswith(id):
                deleted = True
            else:
                file.write(line)
    
    if deleted:
        print(f"Student {id} deleted successfully.")
    else:
        print("Student ID not found.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Display Students")
        print("2. Add Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
