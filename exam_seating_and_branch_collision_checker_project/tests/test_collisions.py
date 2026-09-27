from seating_plan.student import Student
from seating_plan.allocator import create_seating_matrix
from seating_plan.checker import count_collisions

def run_tests():
    # Create 3 students (2 CSE sitting next to each other, 1 ECE)
    test_students = [
        Student(1, "Aman", "CSE"),
        Student(2, "Rahul", "CSE"),
        Student(3, "Priya", "ECE")
    ]
    
    # Put them in a 1-row, 3-column grid
    test_grid = create_seating_matrix(test_students, 1, 3)
    
    # Count clashes (should be 1 between Aman and Rahul)
    clashes = count_collisions(test_grid, 1, 3)
    
    # Check if logic worked using standard if-else
    if clashes == 1:
        print("SUCCESS: Collision test passed successfully!")
    else:
        print("FAILURE: Collision count is incorrect.")

if __name__ == "__main__":
    run_tests()