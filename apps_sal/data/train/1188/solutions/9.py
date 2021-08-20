t = int(input())
l = [0] * (t + 1)
arr = list(map(int, input().split()))
for i in arr:
    if i != 0:
        l[i] += 1
ans = ''
for i in range(1, t + 1):
    if l[i] == 0:
        ans += str(i) + ' '
print(ans)
