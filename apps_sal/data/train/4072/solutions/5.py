def permutation_position(perm):
    a = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, }
    perm = perm.lower()
    b = 0
    y = 1
    z = []
    while b < len(perm) - 1:
        z.append((a[perm[b]] - 1) * (26 ** (len(perm) - y)))
        b = b + 1
        y = y + 1
    z.append(a[perm[-1]])
    return sum(z)
