from math import factorial
from functools import reduce

lst = [1] * (10**6 + 1)

for j in range(1, 10**6 + 1):
    lst[j] = (lst[j - 1] * j) % (10**9 + 7)
for j in range(1, 10**6 + 1):
    lst[j] = (lst[j - 1] * lst[j]) % (10**9 + 7)
for i in range(int(input())):
    n = int(input())
    x = lst[n]
    print(x % (10**9 + 7))
