def has_exit(maze):
    N, M = len(maze)+2, len(maze[0])+2
    maze = ['b'*M] + ['b'+row+'b' for row in maze] + ['b'*M]
    q = [(i,j) for i,row in enumerate(maze) for j,c in enumerate(row) if c == 'k']
    if len(q) != 1: raise Exception('Wrong number of Kates')
    v = set(q)
    while q:
        i,j = q.pop()
        nbs = [(i+a,j+b,maze[i+a][j+b]) for a in range(-1,2) for b in range(-1,2) if bool(a) != bool(b)]
        for ni,nj,nv in nbs:
            if nv == 'b': return True
            if nv == '#' or (ni,nj) in v: continue
            q.append((ni,nj)) or v.add((ni,nj))
    return False
