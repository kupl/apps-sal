# cook your dish here
t=int(input())
while t>0 :
 n,k=map(int,input().split())
 l=list(map(int,input().split()))
 dis=len(set(l))
 a=0
 for i in range(n-k+1) :
  ls=[]
  s=0
  for j in range(k) :
   s+=l[i+j]
   if l[i+j] in ls :
    pass
   else :
    ls.append(l[i+j])
  if len(ls)==dis :
   a=max(a,s)
 print(a)
 t-=1
