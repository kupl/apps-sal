n = int(input())
a = list(map(int, input().split()))
p = [0] * (n + 1)
ans = [1] * (n + 1)
ind = n
for i in range(n):
    p[a[i] - 1] = 1
    while ind > 0 and p[ind - 1] == 1:
        ind -= 1
    ans[i + 1] = 1 + (i + 1) - (n - ind)
print(' '.join(map(str, ans)))
