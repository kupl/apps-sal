for i in range(int(input())):
 n,k=[int(i) for i in input().split()]
 m=input().split()
 for i in range(k):
  if m.pop()=='H':
   for ind,j in enumerate(m):
    if j=='H':
     m[ind]='T'
    else:
     m[ind]='H'
 print(sum([1 for i in m if i=='H']))
