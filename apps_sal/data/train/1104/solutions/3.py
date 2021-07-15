# cook your dish here
"""
Created on Sat May 23 23:48:49 2020

@author: aurouS_EeRiE
"""


def solve(n, k):
    ans = 0
    if n == 0:
        if k == 1:
            return 0
        else:
            return ((k - 1) * (k)) % ((10 ** 9) + 7)
    if k == 1:
        return (n * n) % ((10 ** 9) + 7)
    if k % 2 == 0:
        ans = n * n + n * k + int(int((k - 1) / 2) * int((k - 1) / 2 + 1))
    if k % 2 != 0:
        ans = n * n + (2 * n) * (max(0, int((k - 1) / 2))) + int(int((k - 1) / 2) * int((k - 1) / 2 + 1))
    return ans % ((10 ** 9) + 7)

t = int(input())
for i in range(t):
    n, k=map(int, input().split())
    print(solve(n, k))
