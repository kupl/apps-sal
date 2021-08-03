def rotate(matrix):
    return list(zip(*matrix[::-1]))


def how_many_bees(hive):
    if hive:
        s1 = " ".join(["".join(r) for r in hive])
        s2 = " ".join(["".join(el) for el in rotate(hive)])
        s = s1 + " " + s2
        return s.count("bee") + s.count("eeb")
    return 0
