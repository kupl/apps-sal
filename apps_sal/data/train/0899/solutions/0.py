from math import ceil

for _ in range(int(input())):
 n = int(input())
 arr = [int(x) for x in input().split()]
 sarr = sum(arr)
 mavg = sarr/n
 while n>1:
  sarr -= arr.pop()
  n-=1
  mavg = max(mavg, sarr/n)
 print(int(ceil(mavg)))
