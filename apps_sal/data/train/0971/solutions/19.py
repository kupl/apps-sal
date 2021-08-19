# cook your dish here
from collections import Counter
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    c = dict(Counter(a))
    m = max(list(c.values()))
    print(n - m)
