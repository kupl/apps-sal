# cook your dish here
from itertools import combinations
a = list(map(int, input().split()))
n = a[0]
t = a[1]
q = list(combinations(a[2:], 4))
total = 0
for i in q:
    if sum(i) == t:
        total += 1
print(total)

