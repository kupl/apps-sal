def puzzle_solver(pieces, w, h):
    memo, D, result = {}, {None: (None, None)}, [[None]*w for _ in range(h)]
    
    for (a, b), (c, d), id in pieces:
        memo[(a, b, c)] = id
        D[id] = (c, d)
    
    for i in range(h):
        for j in range(w):
            a, b = D[result[i-1][j]]
            _, c = D[result[i][j-1]]
            result[i][j] = memo[(a, b, c)]
    
    return list(map(tuple, result))
