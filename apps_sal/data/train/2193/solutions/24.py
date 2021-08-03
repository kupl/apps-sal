USE_STDIO = False

if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    n, = list(map(int, input().split(' ')))
    scores = []
    for id in range(n):
        scores.append((-sum(map(int, input().split(' '))), id))
    scores.sort()
    for rank in range(n):
        if scores[rank][1] == 0:
            print(rank + 1)
            return


def __starting_point():
    main()


__starting_point()
