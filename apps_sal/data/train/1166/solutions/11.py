from sys import stdin, stdout
import numpy as np
n = int(input())
a = list(map(int, input().split()))
q = int(input())
while q:
    q -= 1
    k = int(input())
    ans = 0
    for i in range(n):
        flag = False
        count = 0
        forward = 0
        backward = 1
        if a[i] == k:
            if i != a.index(k):
                flag = True
            for j in range(i, n):
                if a[j] >= k:
                    forward += 1
                else:
                    break
            for j in range(i - 1, -1, -1):
                if flag:
                    if a[j] > k:
                        backward += 1
                    else:
                        break
                elif a[j] >= k:
                    backward += 1
                else:
                    break
            count += forward * backward
            ans += count
    print(ans)
