for _ in range(int(input())):
 n,k,x,y = map(int,input().split())
 if x==y:
  print(n,n)
 else:
  l = []
  if x<y:
   l = [[n-y+x,n],[n,n-y+x],[y-x,0],[0,y-x]]
  else:
   l = [[n,y+n-x],[y+n-x,n],[0,x-y],[x-y,0]]
  var = l[(k-1)%4]
  print(var[0],var[1])
