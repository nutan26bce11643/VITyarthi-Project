"""

Exam Seating Matrix & Branch Collision Checker

Course: Python Essentials - Evaluated Course Project

Course Modules Applied:
- Module 7 (Data Structures): 2D lists/matrices for classroom grid
- Module 8 (Control Flow): Nested for loops and if-else condition checks
- Module 9 (Functions): Reusable functions with parameters and return values
- Module 10 (Modules & Packages): Custom package structure (seating_plan)
- Module 12 (OOP): Object oriented programming Student class
"""

# Import statements
from seating_plan.student import Student
from seating_plan.allocator import create_seating_matrix
from seating_plan.checker import count_collisions
from seating_plan.display import show_seating_plan
from tests.test_collisions import run_tests

if __name__ == "__main__":
    # Sample student input
    student_list = [
        Student(101, "Aman", "CSE"),
        Student(102, "Rohan", "CSE"),
        Student(103, "Priya", "ECE"),
        Student(104, "Karan", "MECH"),
        Student(105, "Neha", "ECE"),
        Student(106, "Sunaina", "CSE"),
        Student(107, "Shriya", "MECH"),
        Student(108, "Rakesh", "CIV"),
        Student(109, "Himesh", "CSE"),
        Student(110, "Trisha", "CSE")
    ]

    # Grid size for exam hall
    rows = 4
    cols = 3

    # Generate and print seating matrix arrangement
    exam_grid = create_seating_matrix(student_list, rows, cols)
    show_seating_plan(exam_grid, rows, cols)

    # Count adjacent same-branch seat clashes
    total_clashes = count_collisions(exam_grid, rows, cols)
    print(f"Total same-branch clashes found: {total_clashes}")

    # Testing section
    print("\nTesting")
    print("Running test script to check if collision checker works properly.")
    run_tests()
