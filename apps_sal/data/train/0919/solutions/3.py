t = int(input())

for _ in range(t):
 n = int(input())
 l = list(map(int,input().split()))
 
 s = set()
 
 count = 0
 for i in l:
  if i in s:
   count += 2
   s.clear()
  else:
   s.add(i)
 
 print(n-count)
