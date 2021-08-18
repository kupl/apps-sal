

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [(a, i + 1) for i, a in enumerate(A)]
    B.sort(reverse=True)
    B.append((0, 0))
    ans = [0] * (N + 1)
    idx = N + 1
    for i in range(N):
        add = (i + 1) * (B[i][0] - B[i + 1][0])
        idx = min(idx, B[i][1])
        ans[idx] += add
    print(*ans[1:], sep="\n")


def __starting_point():
    main()


__starting_point()
