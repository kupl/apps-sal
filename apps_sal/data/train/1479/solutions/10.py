# cook your dish here
for _ in range(int(input())):
 n=int(input())
 l=[]
 d=dict()
 for i in range(n):
  l=[int(i) for i in input().split()]
  if l[0] in [1,2,3,4,5,6,7,8]:
   if l[0] in list(d.keys()):
    if d[l[0]]<l[1]:
     d[l[0]]=l[1]
   else:
    d[l[0]]=l[1]
 s=0
 for i,j in list(d.items()):
  s=s+j
 print(s)

