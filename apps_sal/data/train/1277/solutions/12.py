n=int(input())
for i in range(n):
  n1=int(input())
  loss=0
  for j in range(n1):
    l=list(map(int,input().split()))
    loss+=(l[1]*l[0]*(l[2]*l[2]))/10000
    
  print(loss)
