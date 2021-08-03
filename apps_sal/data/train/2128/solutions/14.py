n = int(input())
l = [int(i) for i in input().split()]
zeroes = [0] * n
if l[-1] == 0:
    zeroes[n - 1] = 1
else:
    zeroes[n - 1] = 0
for i in range(n - 2, -1, -1):
    zeroes[i] = zeroes[i + 1]
    if l[i] == 0:
        zeroes[i] += 1
cnt = 0
for i in range(n):
    if l[i] == 1:
        cnt += zeroes[i]
print(cnt)
