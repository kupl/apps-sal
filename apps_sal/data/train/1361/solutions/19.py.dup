# cook your dish here
from itertools import accumulate
n, k = map(int, input().split())
lst = list(map(int, input().split()))
temp = (10**9) + 7
for i in range(k):
    lst = list(accumulate(lst))
for i in lst:
    print(i % (temp), end=' ')
