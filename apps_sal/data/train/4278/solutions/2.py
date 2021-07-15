def diagonal(matrix):
    l=len(matrix)
    pd=sum(matrix[i][i] for i in range(l))
    sd=sum(matrix[i][l-i-1] for i in range(l))
    return (["Principal Diagonal win!","Secondary Diagonal win!","Draw!"]
    [0 if pd>sd else 1 if pd<sd else 2])

