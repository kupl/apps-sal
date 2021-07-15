# cook your dish here
from math import ceil
tc = int(input())
sw = list(map(int, input().split()))
sw.sort()
b = list(set(sw))
sol = 0
for i in b:
 sol = sol + ceil(sw.count(i)/2)
print(sol)
