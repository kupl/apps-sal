def solve(l):
    m = l.index(max(l))
    if m == 0 or m == len(l) - 1:
        return 1
    return 1 + min(solve(l[0:m]), solve(l[m + 1:]))


tc = int(input())
for test in range(tc):
    n = int(input())
    l = list(map(int, input().split()))
    print(solve(l))
