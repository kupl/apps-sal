def ant_bridge(ants, terrain):
    q = [ c for c in ants ]
    terrain = [ c for c in terrain ] + ['-']
    for i in range(len(terrain)-1):
        if terrain[i] == '-' and terrain[i+1] == '.':
                terrain[i] = q.pop()
                q.insert(0, terrain[i])
        elif terrain[i] == '.':
            terrain[i] = q.pop()
            q.insert(0, terrain[i])
            if terrain[i+1] == '-':
                terrain[i+1] = q.pop()
                q.insert(0, terrain[i+1])

    rest = "".join(q)
    return rest

