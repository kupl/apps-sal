t=int(input())
for _ in range(t):
 n = int(input())
 l = list(map(int,input().split()))
 s = list(set(l))
 sum = 0 
 for i in s:
  x = l.count(i)
  if x>sum:
   sum=x 
 print(len(l)-sum) 
