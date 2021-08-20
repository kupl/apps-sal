def play_OX_3D(moves):
    d = ([], [])
    for (n, (x, y, z)) in enumerate(moves, 1):
        c = d[n % 2]
        c += zip(range(13), (x, x, y, x, x, y, y, z, z, x + y, y + x, z + x, x - y), (y, z, z, y + z, y - z, x + z, x - z, x + y, x - y, x + z, y + z, z + y, y - z))
        if 4 in map(c.count, c):
            return 'XO'[n % 2] + ' wins after %d moves' % n
    return 'No winner'
