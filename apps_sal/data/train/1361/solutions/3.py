# cook your dish here
from itertools import accumulate
N, K = map(int, input().split())
l = list(map(int, input().split()))
t = (10**9) + 7
for i in range(K):
    l = list(accumulate(l))
for i in l:
    print(i % (t), end=' ')
