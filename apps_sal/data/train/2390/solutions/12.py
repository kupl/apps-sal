import sys
input = sys.stdin.readline


def ecount(X):
    (c, ans) = (1, [])
    for i in range(len(X) - 1):
        if X[i] == X[i + 1]:
            c += 1
        else:
            ans.append(c)
            c = 1
    ans.append(c)
    return ans


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = ecount(a)
    b.sort(reverse=1)
    ans = b[0]
    m = b[0]
    for i in b[1:]:
        m = min(max(0, m - 1), i)
        ans += m
    print(ans)
