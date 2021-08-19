from math import sqrt
[n, h] = list(map(int, input().split()))
ans = ''
for i in range(1, n):
    ans = ans + str(sqrt(i / n) * h) + ' '
print(ans)
