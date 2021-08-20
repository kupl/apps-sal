n = int(input())
a = sorted(list(set(map(int, input().split()))))
n = len(a)
lb = [0] + [-1] * 2000000
for x in a:
    lb[x] = x
for i in range(1, 2000001):
    if lb[i] == -1:
        lb[i] = lb[i - 1]
ans = 0
for i in range(n):
    for j in range(2, 2000000):
        if a[i] * j > 1000000:
            ans = max(ans, a[-1] % a[i])
            break
        else:
            ans = max(ans, lb[j * a[i] - 1] % a[i])
print(ans)
