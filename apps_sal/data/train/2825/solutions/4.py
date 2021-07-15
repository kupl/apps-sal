def even_magic(n):
    sq = [[y*n+x+1 for x in range(n)] for y in range(n)]
    
    for x in range(n):
        for y in range(n):
            if y % 4 == x % 4 or y % 4 == 3-x % 4:
                sq[x][y] = n**2 + 1 - sq[x][y]
    return sq

