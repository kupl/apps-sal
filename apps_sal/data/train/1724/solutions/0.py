def blast_sequence(aliensStart, position):

    def moveAliens(aliens, furthest):
        lst, shootPath = [], []
        for x, y, s in aliens:
            y += s
            if not (0 <= y < N):
                x, s = x + 1, -s
                y = -y - 1 if y < 0 else 2 * N - y - 1
            (shootPath if y == Y else lst).append((x, y, s))
            if x > furthest:
                furthest = x
        return lst, shootPath, furthest

    def shootTarget(shootPath):
        if shootPath:
            z = max(shootPath, key=lambda a: (a[0], abs(a[2]), a[2]))
            shootPath.remove(z)
            shots.append(turn)

    (X, Y), N = position, len(aliensStart[0])
    aliens = [(x, y, s) for x, r in enumerate(aliensStart) for y, s in enumerate(r) if s]
    shots, furthest, turn = [], 0, -1

    while aliens and furthest < X:
        turn += 1
        aliens, shootPath, furthest = moveAliens(aliens, furthest)
        shootTarget(shootPath)
        aliens += shootPath

    return shots if not aliens else None
