import fileinput


def CountMax(nA, A):
    hT = {}
    for n in A:
        if n not in hT:
            hT.setdefault(n, 1)
        else:
            hT[n] += 1
    vals = [(pair[0], pair[1]) for pair in hT.items()]
    vals.sort(key=lambda p: p[0])
    return max(vals, key=lambda p: p[1])


def main():
    f = fileinput.FileInput()
    r = f.readline()
    if (r == ''):
        return 0
    else:
        nT = int(r)
    while nT > 0:
        nA = int(f.readline())
        A = list(map(int, (f.readline().strip()).split(' ')))
        result = CountMax(nA, A)
        print(result[0], result[1])
        nT = nT - 1
    return 0


def __starting_point():
    main()


__starting_point()
