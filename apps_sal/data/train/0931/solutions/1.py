def bit(x):
    s = 0
    for i in range(len(x)):
        p = bool((x[i] & (1 << (0))))
        if(p == False):
            s = s + x[i]
    return s


def __starting_point():
    n = int(input())
    for i in range(n):
        a = int(input())
        x = list(map(int, input().split()))
        print(bit(x))


__starting_point()
