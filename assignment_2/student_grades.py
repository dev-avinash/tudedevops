#!/usr/bin/env python3
"""Task 2: Student Grades.

Store student names (keys) and grades (values) in a dictionary and let the
user add a student, update an existing student's grade, or print everyone.
"""

students = {}


def add_student():
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    if name in students:
        print(f"{name} already exists. Use the update option instead.")
    else:
        students[name] = grade
        print(f"Added {name} with grade {grade}.")


def update_student():
    name = input("Enter student name to update: ")
    if name in students:
        students[name] = input("Enter new grade: ")
        print(f"Updated {name}'s grade to {students[name]}.")
    else:
        print(f"{name} not found. Use the add option first.")


def print_grades():
    if not students:
        print("No students yet.")
    else:
        print("--- Student Grades ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")


def main():
    while True:
        print("\n1. Add student  2. Update grade  3. Print all  4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            print_grades()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
