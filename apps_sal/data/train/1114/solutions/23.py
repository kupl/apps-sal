# cook your dish here
try:
 t = int(input())
 for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  from itertools import combinations
  ans = []
  for l in combinations(arr,2):
   ans.append(l)
  maxx = 0
  for l in ans:
   m = sum(l)
   if m>maxx:
    maxx = m
  count = 0 
  for l in ans:
   item = sum(l)
   if item<maxx:
    count+=1
  print(1 - count/len(ans))
  continue
except:
 pass
  
 

