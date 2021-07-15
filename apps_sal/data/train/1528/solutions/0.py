t=int(input())
for i in range(t):
 n,k=[int(i) for i in input().split()]
 l=input().split()
 for i in range(k):
  if l.pop()=='H':
   for ind,j in enumerate(l):
    if j=='H':
     l[ind]='T'
    else:
     l[ind]='H'
 print(sum([1 for i in l if i=='H']))
