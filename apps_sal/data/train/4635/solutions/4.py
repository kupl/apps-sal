def create_octahedron(size):
    if size % 2 == 0 or size <= 1:
        return []
    r1, r2, r3 = [], [], []

    for i in range(size // 2 + 1):
        for j in range(size):
            for k in range(size):

                if j - i <= k <= j + i and size - j - 1 - i <= k <= size - j - 1 + i:
                    r3.append(1)
                else:
                    r3.append(0)
            r2.append(r3)
            r3 = []
        r1.append(r2)
        r2 = []

    for i in range(size // 2 - 1, -1, -1):
        r1.append(r1[i])

    return r1
