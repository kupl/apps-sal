def trace(matrix):
    if matrix and set(map(len,matrix))=={len(matrix)}:
        return sum(matrix[x][x] for x in range(len(matrix)))
