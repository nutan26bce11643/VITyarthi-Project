# Exam Seating Matrix & Branch Collision Checker
from seating_plan.student import Student
from seating_plan.allocator import create_seating_matrix
from seating_plan.checker import count_collisions
from seating_plan.display import show_seating_plan

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
