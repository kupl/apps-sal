def blast_sequence(aliensStart,position):
    
    def moveAliens(aliens, furthest):
        lst, shootPath = [], []
        for x,y,s in aliens:
            y += s
            if not (0 <= y < N):                                           #Out of the grid: move down and reverse
                x, s = x+1, -s
                y = -y-1 if y < 0 else 2*N-y-1
            (shootPath if y == Y else lst).append((x,y,s))
            if x > furthest: furthest = x
        return lst, shootPath, furthest
    
    def shootTarget(shootPath):
        if shootPath:
            z = max(shootPath, key=lambda a: (a[0], abs(a[2]), a[2]))     # Furthest, fastest, going right is considered the highest
            shootPath.remove(z)                                           # MUTATION
            shots.append(turn)                                            # MUTATION
    
    (X,Y), N = position, len(aliensStart[0])
    aliens   = [(x,y,s) for x,r in enumerate(aliensStart) for y,s in enumerate(r) if s]
    shots, furthest, turn = [], 0, -1
    
    while aliens and furthest < X:
        turn += 1
        aliens, shootPath, furthest = moveAliens(aliens, furthest)        # Move all the aliens, splitting them in 2 groups: those facing "my" ship (shootPath) and the others
        shootTarget(shootPath)                                            # Extract the target in shootPath and pop it if possible (mutation). Mutate 'shots' list at the same time
        aliens += shootPath                                               # Put the remaining aliens in the list
    
    return shots if not aliens else None
