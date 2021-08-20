n = int(input())
m = list(map(int, input().split()))
q = int(input())
for case in range(q):
    (l, r) = list(map(int, input().split()))
    l = l - 1
    r = r - 1
    s = m[l:r + 1]
    s.sort()
    ans = 0
    for i in range(r - l):
        ans = ans + (s[i + 1] - s[i]) ** 2
    print(ans)
