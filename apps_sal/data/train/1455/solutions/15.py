n = int(input())
a = list(map(int, input().split()))
for q in range(int(input())):
    (l, r) = list(map(int, input().split()))
    s = sorted(a[l - 1:r])
    ans = 0
    for i in range(r - l):
        ans += (s[i + 1] - s[i]) ** 2
    print(ans)
