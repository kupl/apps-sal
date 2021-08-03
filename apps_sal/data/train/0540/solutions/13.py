def main():
    n, m = [int(x) for x in input().split()]
    l = [int(X) for X in input().split()]
    ls = set(l)
    f = 1
    for i in range(1, m):
        if i not in ls:
            f = 0
            break
    if f == 0:
        print(-1)
    else:
        if m in ls:
            print(n - l.count(m))
        else:
            print(n)


def __starting_point():
    for _ in range(int(input())):
        main()


__starting_point()
