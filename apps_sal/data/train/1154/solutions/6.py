def amongus(n, f, d):
    for i in range(n):
        if f[i] != d[i]:
            return d[i]
    return d[-1]


def __starting_point():
    n = int(input())
    f = list(map(int, input().strip().split()))
    d = list(map(int, input().strip().split()))
    f.sort()
    d.sort()
    print(amongus(n, f, d))


__starting_point()
