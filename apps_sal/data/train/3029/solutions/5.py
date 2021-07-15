import numpy as np

def levenshtein(s,t):
    #create a matrix.
    m, n = len(s) , len(t)
    table = np.zeros((m, n), dtype=int)
    # first column
    for i in range(m):
        for j in range(n):
            # for first column.
            if j == 0:
                if i == 0:
                    if s[i] == t[j]:
                        table[i][j] = 0
                    else:
                        table[i][j] = 1
                if i > 0:                    
                    if s[i] == t[j]:                    
                        table[i][j] = table[i - 1][j]
                    else:                   
                        table[i][j] = table[i - 1][j] + 1
            else:
                # and first line.
                if i == 0:
                    if s[i] == t[j]:
                        table[i][j] =  table[i][j - 1]
                    else:
                        if j > 0:                            
                            table[i][j] = table[i][j - 1] + 1
                else:
                    # for others
                    if s[i] == t[j]:
                        table[i][j] =  table[i - 1][j - 1]
                    else:
                        table[i][j] = min(table[i][j - 1], table[i -1][j],table[i - 1][j - 1]) + 1 
    print(table)
    return table[-1][-1]
