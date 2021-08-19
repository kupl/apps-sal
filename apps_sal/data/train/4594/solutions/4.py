def transpose(matrix):
    transp = []
    for i in range(len(matrix[0])):
        transp.append([matrix[j][i] for j in range(len(matrix))])
    return transp
