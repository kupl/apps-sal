from collections import defaultdict
from itertools import combinations

def norm(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve():
    houses = []
    n,m = list(map(int, input().split()))
 
    for i in range(n):
     s = input()
     tmp = [i for i,x in enumerate(s) if x =='1']
     houses = houses + [(i,j) for j in tmp]
 
    counter = defaultdict(int)
    for a,b in combinations(houses,2):
     counter[norm(a,b)] += 1
    return [counter[i] for i in range(1,n+m-1)]

for _ in range(int(input())):
    print(*solve())
