# cook your dish here
n, x = map(int, input().split())
l = list(map(int, input().split()))
ans = l[0]
temp = l[0]
for i in range(1, n):
    temp = max(l[i], temp + l[i])
    ans = max(temp, ans)
print(sum(l) - ans + (ans / x))
