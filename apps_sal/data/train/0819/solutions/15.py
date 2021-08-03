def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x


def __starting_point():
    for _ in range(int(input())):
        x, y = list(map(int, input().split()))
        if hcf(x, y) == 1:
            print("YES")
        else:
            print("NO")


__starting_point()
