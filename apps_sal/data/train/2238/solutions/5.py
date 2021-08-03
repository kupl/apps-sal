def solve():
    a, b = [int(x) for x in input().split()]
    l = b - a + 1
    for i in range(64):
        if a & (1 << i):
            continue
        if (a | (1 << i)) > b:
            break
        a |= 1 << i
    print(a)


n = int(input())
for i in range(n):
    solve()
