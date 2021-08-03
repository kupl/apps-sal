def face(size, m, n):
    return [
        [abs(r - m) + abs(c - m) <= n for c in range(size)]
        for r in range(size)
    ]


def create_octahedron(size):
    if size == 1 or size % 2 == 0:
        return []
    m = size // 2
    return [face(size, m, min(i, size - 1 - i)) for i in range(size)]
