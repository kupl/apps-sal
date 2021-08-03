def triangle(inp):
    kek = inp
    while len(kek) != 1:
        mek = []
        for c1, c2 in zip(kek, kek[1:]):
            if c1 == c2:
                mek.append(c1)
            else:
                lol = ['R', 'G', 'B']
                lol.remove(c1)
                lol.remove(c2)
                mek.append(*lol)
        kek = mek
    return kek[0]
