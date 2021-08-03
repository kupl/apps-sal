def p(l):
    n2 = len(l)
    m = l.index(max(l))
    if m < 1 or m > n2 - 2:
        return 1
    return 1 + min(p(l[:m]), p(l[m + 1:]))


t = int(input())
solution = []
for r in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solution.append(p(a))
print(*solution, sep="\n")
