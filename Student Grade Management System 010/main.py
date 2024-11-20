from grade import Grade

def main():
    student1 = Grade(1, "John Doe", 85)
    student2 = Grade(2, "Jane Smith", 92)
    student3 = Grade(3, "Sam Wilson", 45)

    student1.display_result()
    print()
    student2.display_result()
    print()
    student3.display_result()

if __name__ == "__main__":
    main()
