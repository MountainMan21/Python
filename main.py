import json
import os
from datetime import datetime, timedelta
import schedule
from plyer import notification
from notifications import send_notification


class Task:
    def __init__(self, name, priority, due_date, notes=""):
        self.name = name
        self.priority = priority.lower()
        self.due_date = due_date
        self.notes = notes

    def to_dict(self):
        return {
            "name": self.name,
            "priority": self.priority,
            "due_date": self.due_date,
            "notes": self.notes
        }


class ToDoList:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        save_tasks(self)

    def edit_task(self, task_name, new_task):
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                self.tasks[i] = new_task
                save_tasks(self)
                return True
        return False

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]
        save_tasks(self)

    def view_tasks(self, filter_by=None):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        if filter_by == "high_priority":
            return [task for task in self.tasks if task.priority == "high"]
        elif filter_by == "upcoming":
            return [task for task in self.tasks if task.due_date >= current_time]
        return self.tasks


def save_tasks(todo_list, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump([task.to_dict() for task in todo_list.tasks], f, indent=4)


def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            tasks_data = json.load(f)
            return [Task(**data) for data in tasks_data]
    except FileNotFoundError:
        return []


def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('-'))
        due_date = datetime(year, month, day)

        if due_date < datetime.now() or due_date > datetime.now() + timedelta(days=365):
            raise ValueError("Date must be within 1 year from now.")

        return due_date.strftime("%Y-%m-%d %H:%M")  # Return formatted date string
    except (ValueError, IndexError):
        raise ValueError("Invalid date format. Please use DD-MM-YYYY format.")


def check_deadlines(todo_list):
    current_time = datetime.now()
    for task in todo_list.tasks:
        try:
            due_time = datetime.strptime(task.due_date, "%Y-%m-%d %H:%M")
            if due_time <= current_time:
                send_notification(
                    "Task Due",
                    f"Reminder: {task.name} is due now."
                )
            elif (due_time - current_time).days > 365:
                print(f"Unrealistic due date for task '{task.name}': {task.due_date}")

        except ValueError:
            print(f"Invalid due date format for task '{task.name}': {task.due_date}")


def main():
    print(f"Running on: {os.name}")  # Display the OS name
    todo_list = ToDoList()

    # Schedule the deadline check but do not call it automatically
    schedule.every(1).minutes.do(check_deadlines, todo_list)

    while True:
        schedule.run_pending()
        print("\nWelcome to To-Do List Manager!")
        print("1. Add a new task")
        print("2. Edit a task")
        print("3. Delete a task")
        print("4. View all tasks")
        print("5. View high-priority tasks")
        print("6. View upcoming tasks")
        print("7. Show notifications")
        print("8. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (High, Medium, Low): ").lower()
            due_date = input("Enter due date (DD-MM-YYYY HH:MM): ")
            notes = input("Enter additional notes (optional): ")

            try:
                valid_date = is_valid_date(due_date[:10])
                new_task = Task(name, priority, valid_date, notes)
                todo_list.add_task(new_task)
            except ValueError as e:
                print(e)

        elif choice == "2":
            task_name = input("Enter the task name to edit: ")
            name = input("Enter new task name: ")
            priority = input("Enter new priority (High, Medium, Low): ").lower()
            due_date = input("Enter new due date (DD-MM-YYYY HH:MM): ")
            notes = input("Enter new notes (optional): ")

            try:
                valid_date = is_valid_date(due_date[:10])
                new_task = Task(name, priority, valid_date, notes)
                if not todo_list.edit_task(task_name, new_task):
                    print("Task not found.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            task_name = input("Enter the task name to delete: ")
            todo_list.delete_task(task_name)

        elif choice == "4":
            tasks = todo_list.view_tasks()
            for task in tasks:
                print(f"Task: {task.name}, Priority: {task.priority}, Due: {task.due_date}, Notes: {task.notes}")

        elif choice == "5":
            high_priority_tasks = todo_list.view_tasks("high_priority")
            for task in high_priority_tasks:
                print(f"Task: {task.name}, Priority: {task.priority}, Due: {task.due_date}, Notes: {task.notes}")

        elif choice == "6":
            upcoming_tasks = todo_list.view_tasks("upcoming")
            for task in upcoming_tasks:
                print(f"Task: {task.name}, Priority: {task.priority}, Due: {task.due_date}, Notes: {task.notes}")

        elif choice == "7":
            # Send notifications for all tasks
            for task in todo_list.tasks:
                due_time = datetime.strptime(task.due_date, "%Y-%m-%d %H:%M")
                if due_time <= datetime.now():
                    send_notification(
                        "Task Due",
                        f"Reminder: {task.name} is due now."
                    )
            print("Notifications for due tasks sent.")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
