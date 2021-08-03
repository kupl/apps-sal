def main():
    n, k = list(map(int, input().split()))
    res = 0
    for _ in range(k):
        tmp = list(map(int, input().split()))
        if tmp[1] == 1:
            tmp[0] = 0
            for i, x in enumerate(tmp):
                if i != x:
                    res += (len(tmp) - i) * 2
                    break
        else:
            res += len(tmp) * 2 - 3
    print(res)


def __starting_point():
    main()


__starting_point()
