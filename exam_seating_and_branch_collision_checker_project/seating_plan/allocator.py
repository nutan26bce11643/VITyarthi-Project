# Function to create and fill a 2D seating matrix with students
def create_seating_matrix(students,rows,cols):
    # step:1 :cretae an empty matrix filled with "Empty" strings
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("Empty")
        matrix.append(row)
    
    # step:2 :Fill students into the matrix row by row
    index = 0
    for i in range(rows):
        for j in range(cols):
            if index < len(students):
                matrix[i][j] = students[index]
                index += 1
                
    return matrix