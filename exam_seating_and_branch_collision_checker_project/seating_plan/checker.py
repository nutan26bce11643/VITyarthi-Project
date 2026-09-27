# Function to count same-branch students sitting next to each other
def count_collisions(matrix, rows, cols):
    collisions = 0
    
    for i in range(rows):
        for j in range(cols):
            current = matrix[i][j]
            
            # Skip if seat has no student
            if current == "Empty":
                continue
            
            # Check student on the right
            if j + 1 < cols and matrix[i][j + 1] != "Empty":
                if current.branch == matrix[i][j + 1].branch:
                    collisions += 1
            
            # Check student directly below
            if i + 1 < rows and matrix[i + 1][j] != "Empty":
                if current.branch == matrix[i + 1][j].branch:
                    collisions += 1
                    
    return collisions