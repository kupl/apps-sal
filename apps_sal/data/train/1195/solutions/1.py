t = int(input())
for _ in range(t):
 n,a,b,c,d,p,q,y = list(map(int,input().split()))
 lst = list(map(int,input().split()))
 dist1 = abs(lst[a-1]-lst[b-1])
 walk = dist1*p
 acdist = abs(lst[a-1]-lst[c-1])*p
 dist2 = abs(lst[c-1]-lst[d-1])
 dist3 = abs(lst[b-1]-lst[d-1])
 cdtime = dist2*q
 bdtime = dist3*p
 train = y+cdtime+bdtime
 if(acdist<=y):
  print(min(walk,train))
 else:
  print(walk)
  
  

