t = int(input())
for _ in range(t):
 N, K, x, y = list(map(int, input().split()))
 
 if x == y:
  print(N,N)
  
 else:
  temp = []
  if x > y :
   temp = [[N,N-x+y],[N-x+y,N],[0,x-y],[x-y,0]]
  else:
   temp = [[x+N-y,N],[N,N-y+x],[y-x,0],[0,y-x]]
  
  ans = temp[(K-1)%4]
  print(*ans)

