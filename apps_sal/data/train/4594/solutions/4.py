def transpose(matrix):
    transp = []
    #col_m = len(matrix[0])
    #row_m = len(matrix)

    for i in range(len(matrix[0])):

        transp.append([matrix[j][i] for j in range(len(matrix))])

    return transp
