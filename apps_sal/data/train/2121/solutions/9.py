import sys
import math
n = int(input())
a = sorted(list(int(sys.stdin.readline()) for i in range(n)))
i = (n // 2) - 1
j = n - 1
k = 0
while j > ((n // 2) - 1) and i >= 0:
    if 2 * a[i] <= a[j]:
        j -= 1
        k += 1
    i -= 1
print(n - k)
