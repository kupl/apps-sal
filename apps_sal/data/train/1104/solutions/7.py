"""
Created on Sat May 23 23:28:42 2020

Title: Walking Man

Contest: LockDown Test 4.0

@author: mr._white_hat_
"""
for _ in range(int(input())):
    (n, k) = map(int, input().split())
    if n == 0:
        print(k * (k - 1) % 1000000007)
        continue
    x = int((k - k % 2) / 2)
    ans = (n + x - 1) * (n + x) + n + 2 * (k % 2) * x
    print(ans % 1000000007)
