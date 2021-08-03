def main():
    n, m = list(map(int, input().split()))
    alive, winner = list(range(1, n + 3)), [0] * (n + 2)
    for _ in range(m):
        l, r, x = list(map(int, input().split()))
        while l < x:
            if winner[l]:
                alive[l], l = x, alive[l]
            else:
                alive[l] = winner[l] = x
                l += 1
        l += 1
        r += 1
        while l < r:
            if winner[l]:
                alive[l], l = r, alive[l]
            else:
                alive[l], winner[l] = r, x
                l += 1
    print(' '.join(map(str, winner[1: -1])))


def __starting_point():
    main()


__starting_point()
