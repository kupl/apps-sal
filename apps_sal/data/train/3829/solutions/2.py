def build_square(arr):
    c = 0

    def purge(*sizes):
        nonlocal c
        used = []
        try:
            for s in sizes:
                arr.remove(s)
                used.append(s)
            c += 1
        except:
            arr.extend(used)
    for _ in range(16):
        purge(4)
        purge(3, 1)
        purge(2, 2)
        purge(2, 1, 1)
        purge(1, 1, 1, 1)
    return c >= 4
