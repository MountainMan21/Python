class Item:
    def __init__(self, title, category):
        self.title = title
        self.category = category
        self.status = "Available"

    def check_out(self):
        if self.status == "Available":
            self.status = "Checked Out"
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.status == "Checked Out":
            self.status = "Available"
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available.")

    def __str__(self):
        return f"{self.title} ({self.category}) - {self.status}"


class Book(Item):
    def __init__(self, title, author, genre):
        super().__init__(title, "Book")
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Book: {self.title} by {self.author} ({self.genre}) - {self.status}"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def view_items(self):
        if len(self.items) == 0:
            print("No items in the library.")
            return
        for item in self.items:
            print(item)

    def check_out_item(self, title):
        for item in self.items:
            if item.title == title:
                item.check_out()
                return
        print(f"Item with title '{title}' not found.")

    def return_item(self, title):
        for item in self.items:
            if item.title == title:
                item.return_item()
                return
        print(f"Item with title '{title}' not found.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Check Out Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            book = Book(title, author, genre)
            library.add_item(book)
            print(f"Book '{title}' added to the library.")

        elif choice == '2':
            library.view_items()

        elif choice == '3':
            title = input("Enter book title to check out: ")
            library.check_out_item(title)

        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_item(title)

        elif choice == '5':
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
