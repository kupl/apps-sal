def create_octahedron(size):
    if size <= 1 or size % 2 == 0:
        return []
    m = size // 2
    return [[[int(abs(x - m) + abs(y - m) + abs(z - m) <= m) for z in range(size)] for y in range(size)] for x in range(size)]
