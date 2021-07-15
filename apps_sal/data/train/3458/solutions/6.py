def multiplication_table(row,col):
    return [[(i+1)*(j+1) for i in range(col)] for j in range(row)]
