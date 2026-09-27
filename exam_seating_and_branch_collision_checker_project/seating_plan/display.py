# Function to print the classroom seating layout for exam
def show_seating_plan(grid, rows, cols):
    print("\n=== Exam hall Seating Plan ===")
    
    for i in range(rows):
        row_text = f"Row {i + 1}: "
        for j in range(cols):
            seat = grid[i][j]
            if seat == "Empty":
                row_text += "[ Empty ] "
            else:
                row_text += f"[{seat.name}-{seat.branch}] "
        print(row_text)
        
    print("==============================\n")