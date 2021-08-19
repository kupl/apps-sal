import sys
n = int(sys.stdin.readline())
ans = 0
i = -1
n1 = n
while n1 > 0:
    n1 = int(n1 / 2)
    i = i + 1
ans = (n - (1 << i)) * 2 + 1
print(ans)
