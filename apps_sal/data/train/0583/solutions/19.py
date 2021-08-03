# ------- main function -------

def solve():
    n = int(input())
    a = list(map(int, input().split(' ')))
    ls = sum(a)
    if ls >= 0:
        print("YES")
    else:
        print("NO")


# ------- starting point of program -------

def __starting_point():
    for _ in range(int(input())):
        solve()


__starting_point()
