def avg_diags(m):
    n, avg = len(m), [[0,0], [0,0]]
    for i in range(n):
        if i%2 and m[i][i] >= 0:
            avg[0][0] += m[i][i]
            avg[0][1] += 1
        elif not i%2 and m[n-i-1][i] < 0:
            avg[1][0] -= m[n-i-1][i]
            avg[1][1] += 1
            
    return [ round(lst[0]/lst[1]) if lst[1] != 0 else -1 for lst in avg ]
