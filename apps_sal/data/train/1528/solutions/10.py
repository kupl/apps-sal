# cook your dish here
for _ in range(int(input())):
 nk=[int(i) for i in input().split()]
 k=nk[1]
 s=input().split()
 for i in range(k):
  a=s.pop()
  if a=='H':
   for indx,j in enumerate(s):
    if j=='H':
     s[indx]='T'
    else:
     s[indx]='H'
 heads=0
 for i in s:
  if i=='H':
   heads+=1
 print(heads)

