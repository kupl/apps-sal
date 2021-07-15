t = int(input())

for _ in range(t):
 n, k = [int(x) for x in input().split()]
 w = [int(x) for x in input().split()]
 
 i=0
 total = 0
 c = 0
 flag = 0
 
 while(i<n):
  if(w[i] > k):
   flag = 1
   break
  total += w[i]
  if(total > k):
   total = 0
   c += 1
  else:
   i += 1
 
 if(flag == 1):
  print(-1)
 else:
  print(c+1)
