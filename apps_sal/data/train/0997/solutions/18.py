# cook your dish here
import math as ma

N = int(input())
for h in range(N):
    l = list(map(int, input().split()))
    n, q = l
    s = [10]
    s = s * n

    for ques in range(q):
        l = list(map(int, input().split()))
        i, j, k = l
        for p in range(i - 1, j):
            s[p] = s[p] * k
    print(ma.floor(sum(s) / n))
