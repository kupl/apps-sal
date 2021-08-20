from itertools import permutations


def solve(n, a):
    ans = []
    for des in desire:
        check = 1
        for i in range(n - 1):
            if a[i] == a[i + 1]:
                return [-1]
            if a[i + 1] == des[a[i] - 1]:
                check = 0
                break
        if check:
            ans = des
            break
    if ans:
        return ans
    return [-1]


per = permutations([1, 2, 3, 4, 5, 6])
desire = []
for p in per:
    check = 1
    for i in range(1, 7):
        if p[i - 1] == i:
            check = 0
            break
    if check:
        doublecheck = 1
        for i in range(6):
            if p[p[i] - 1] != i + 1:
                doublecheck = 0
                break
        if doublecheck:
            desire.append(p)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(*solve(n, a))
