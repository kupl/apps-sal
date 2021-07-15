def determinant(matrix):
    #your code here
    result = 0
    l = len(matrix)

    #base case when length of matrix is 1
    if l == 1:
        return matrix[0][0]

    #base case when length of matrix is 2
    if l == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    #for length of matrix > 2
    for j in range(0, l):
        # create a sub matrix to find the determinant
        if l!=2:
            sub_matrix = []               
            sub_matrix = [(row[0:j]+row[j+1:]) for row in matrix[1:]]
        result = result + (-1)**j * matrix[0][j] * determinant(sub_matrix)
    return result
