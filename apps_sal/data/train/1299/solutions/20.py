for _ in range(int(input())):
 
 n = int(input())
 l = list(map(int,input().split()))
 
 d = {}
 for ele in set(l):
  d[ele] = 0
   
 i=0 
 while i<n:
  
  count = 0
  type = l[i]
  while l[i] == type:
   count += 1 
   i+=1 
   if i==n:
    break 
  d[type] += (count + 1)//2 
  
 ans = min(l)
 for ele in d:
  if d[ele] > d[ans] or (d[ele] == d[ans] and ans > ele):
   ans = ele
 print(ans)
