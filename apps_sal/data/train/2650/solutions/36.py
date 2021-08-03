def main():
    N, L = list(map(int, input().split()))
    S = []
    for i in range(N):
        s = input()
        S.append(s)
    S.sort()
    ans = ''.join(S)
    print(ans)


def __starting_point():
    main()


__starting_point()
