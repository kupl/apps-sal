# cook your dish here

t=int(input())

for i in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 d={}
 for i in range(n):
  if a[i]-1 not in d:
   d[a[i]-1]=[i]
  else:
   d[a[i]-1].append(i)
 ans=False
 for i in d:
  if ans==True:
   break
  for j in d:
   if ans==True:
    break
   if i!=j:
    if a[i]==a[j] and i!=j:
     
     ans=True
 if ans==True:
  print('Truly Happy')
 else:
  print('Poor Chef')

