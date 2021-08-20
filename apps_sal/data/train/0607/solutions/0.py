"""input
2
3
2 2 3
4
2 3 3 2
"""
import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    i = 0
    while i < len(a):
        if a[i] == 1:
            count += 1
            i += 1
            continue
        curr_gcd = a[i]
        while i < len(a) and curr_gcd != 1:
            curr_gcd = math.gcd(curr_gcd, a[i])
            if curr_gcd == 1:
                count += 1
                i += 1
                break
            i += 1
    print(count)
