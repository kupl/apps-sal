for t in range(int(input())):
 g,t,w=list(map(int,input().split()))
 m=max(g,t,w)
 if((g+t+w-m+1)>=m):
  print('Yes')
 else:
  print('No')

