# Exam Seating & Branch Collision Checker Project
from seating_plan.allocator import create_seating_matrix

if __name__ == "__main__":
    print("--------------------------------------------------")
    print(" Running Exam Seating & Branch Collision Checker")
    print("--------------------------------------------------")
    
    # Sample test data to demonstrate execution
    sample_students = ["Alice_CSE", "Bob_ECE", "Charlie_ME", "David_CSE"]
    print(f"\nInput Students List: {sample_students}")
    
    # Calling the matrix creation function
    seating_result = create_seating_matrix(sample_students, rows=2, cols=2)
    
    print("\nGenerated Seating Arrangement Matrix:")
    for row in seating_result:
        print(row)
        
    print("\nProcess finished successfully!")
