n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pre = [0]
for i in range(n):
    pre.append(pre[-1] + b[i])
maxi = 0
for i in range(n):
    for j in range(n):
        if i == j:
            ans = a[i]
        elif i < j:
            ans = a[i] + a[j] + pre[j] - pre[i + 1]
        else:
            ans = a[i] + a[j] + pre[n] - pre[i + 1] + pre[j]
        maxi = max(ans, maxi)
print(maxi)
