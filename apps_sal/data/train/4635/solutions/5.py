def create_octahedron(size):
    if not (size > 1 and size&1): return []
    res = [[[0]*size for _ in range(size)] for _ in range(size)]
    s = size>>1
    for i in range(-s, s+1):
        x = abs(i)
        for j in range(x-s, s-x+1):
            y = abs(j)
            for k in range(x+y-s, s-x-y+1):
                res[s+i][s+j][s+k] = 1
    return res
