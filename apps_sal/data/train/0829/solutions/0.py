# cook your dish here
# cook your dish here
from itertools import combinations
n = int(input())
t = list(combinations(list(map(int, input().split())), 2))
ar = 0
for i in t:
    ar += abs(i[0] - i[1])
print(ar)
