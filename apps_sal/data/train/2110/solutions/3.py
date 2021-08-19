def main():
    input()
    l = [0] * 1000020
    for w in map(int, input().split()):
        l[w] += 1
    for (w, x) in enumerate(l):
        if x:
            l[w] = x & 1
            while x:
                x >>= 1
                w += 1
                if x & 1:
                    l[w] += 1
    print(sum(l))


def __starting_point():
    main()


__starting_point()
