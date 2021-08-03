from collections import Counter


def solve(A, B):
    a = Counter(A)
    b = Counter(B)
    ans = 0
    for i in a:
        if i in b:
            ans += min(a[i], b[i])

    return ans


t = int(input())

for _ in range(t):
    A = input()
    B = input()
    print(solve(A, B))
