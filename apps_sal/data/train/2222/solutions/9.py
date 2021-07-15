def safe(mat, x, y, n):
    if not x in [0,1,2]:
        return False
    for i in range(1, 4):
        if y+i<n and mat[x][y+i] != '.':
            return False
    return True

def dfs(mat, n):
    pos = 0
    for k in range(3):
        if mat[k][0]=='s':
            pos = k
    vis = {}
    s = [(pos,0)]
    while s:
        x,y = s.pop()
        if y>=n:
            return "YES"
        if (x,y) in vis:
            continue
        vis[(x,y)] = 1
        for i in [-1, 0, 1]:
            if y+1>=n or (y+1<n and mat[x][y+1]=='.' and safe(mat, x+i, y, n)):
                s.append((x+i, y+3))
    return 'NO'
    

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    mat = [input() for i in range(3)]
    print(dfs(mat, n))
