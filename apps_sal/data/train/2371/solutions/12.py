import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    l = int(input())
    m = list(map(int, input().split()))
    m = m[::-1]
    uni = []
    gro = 1
    ok = 1
    ans = 0
    for j in range(len(m) - 1):
        if gro == 0:
            if m[j + 1] > m[j]:
                ok = 0
                ans = j + 1
                break
        if m[j + 1] < m[j]:
            gro = 0
    if ans == 0:
        print(ans)
    else:
        print(l - ans)
