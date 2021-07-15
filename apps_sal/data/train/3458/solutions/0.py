def multiplication_table(row,col):
    return [[(i+1)*(j+1) for j in range(col)] for i in range(row)]
