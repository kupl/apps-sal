import sys

def solve():
    l, r = map(int, input().split())

    if l == r:
        ans = l
    else:
        ans = 2

    print(ans)

def __starting_point():
    solve()
__starting_point()
