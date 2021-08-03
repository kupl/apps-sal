from sys import stdin, stdout
import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
q = int(input())
while q:
    q -= 1
    k = int(input())
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if min(a[i:j]) == k:
                ans += 1
    print(ans)
