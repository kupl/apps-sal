def main():
    (n, k) = list(map(int, input().split()))
    for i in range(k):
        tmp = input().split()
        if tmp[1] == '1':
            tmp.append('0')
            tmp[0] = '0'
            for (i, m) in enumerate(map(int, tmp)):
                if i != m:
                    print((n - i) * 2 - k + 3)
                    return


def __starting_point():
    main()


__starting_point()
