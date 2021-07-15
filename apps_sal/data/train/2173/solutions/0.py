from itertools import starmap


def main():
    n, q = list(map(int, input().split()))

    a = list(range(n + 1))
    flipped = False
    start = 0
    end = n

    for _ in range(q):
        cmd, *args = list(map(int, input().split()))

        if cmd == 1:
            p = args[0]
            if p > end-start-p:
                flipped = not flipped
                p = end-start-p
            if flipped:
                a[end-p:end-2*p:-1] = starmap(
                    lambda a, b: a+n-b,
                    list(zip(a[end-p:end-2*p:-1], a[end-p:end]))
                )
                end -= p
            else:
                start += p
                a[start:start+p] = starmap(
                    lambda a, b: a-b,
                    list(zip(a[start:start+p], a[start:start-p:-1]))
                )
        else:
            l, r = args
            if flipped:
                l, r = end-start-r, end-start-l
            print(a[start + r] - a[start + l])


def __starting_point():
    main()


__starting_point()
