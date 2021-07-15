def how_many_bees(hive):
    if not hive:
        return 0
    
    hive_matrix = [list(line) for line in hive]
    
    max_col = len(hive_matrix[0])
    max_row = len(hive_matrix)
    
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1
    
    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(hive_matrix[y][x])
            rows[y].append(hive_matrix[y][x])
            fdiag[x+y].append(hive_matrix[y][x])
            bdiag[x-y-min_bdiag].append(hive_matrix[y][x])
            
    h1 = '\n'.join([''.join(line) for line in cols])
    h11 = h1.count('bee') + h1.count('eeb')
    
    v1 = '\n'.join([''.join(line) for line in rows])
    v11 = v1.count('bee') + v1.count('eeb')
    
    d1 = '\n'.join(''.join(line) for line in fdiag)
    d11 = d1.count('bee') + d1.count('eeb')
    
    d2 = '\n'.join(''.join(line) for line in bdiag)
    d22 = d2.count('bee') + d2.count('eeb')
    return h11 + v11 + d11 + d22
