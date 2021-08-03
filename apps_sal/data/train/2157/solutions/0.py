def main():
    from heapq import heapify, heapreplace
    input()
    s = set(map(int, input().split()))
    xx = [-x for x in s]
    heapify(xx)
    while True:
        x = -xx[0]
        while x != 1:
            x //= 2
            if x not in s:
                s.add(x)
                heapreplace(xx, -x)
                break
        else:
            break
    print(' '.join(str(-x) for x in xx))


def __starting_point():
    main()


__starting_point()
