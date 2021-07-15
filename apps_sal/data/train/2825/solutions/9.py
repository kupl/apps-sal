def even_magic(n):
    result, n2 = [[n*i+j+1 for j in range(n)] for i in range(n)], n**2
    for x in range(n):
        result[x][x] = n2 + 1 - result[x][x]
        result[x][-x-1] = n2 + 1 - result[x][-x-1]
    for i in range(4, n, 4):
        for x in range(n-i):
            result[i+x][x] = n2 + 1 - result[i+x][x]
            result[x][i+x] = n2 + 1 - result[x][i+x]
            result[x][-x-1-i] = n2 + 1 - result[x][-x-1-i]
            result[i+x][-x-1] = n2 + 1 - result[i+x][-x-1]
    return result
