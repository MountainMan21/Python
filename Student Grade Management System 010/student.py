class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
