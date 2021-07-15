n=int(input())
min1=1000000009
id=0
s=""
for i in range(1,n+1):
  m=(n+i-1)//i
  if (m+i)<min1:
    min1=m+i
    id=i
a=[]
for i in range(n,0,-1):
  a.append(i)
  if(len(a)==id):
    a.reverse()
    for j in range(len(a)):
      s+=str(a[j])+" "
    a.clear()
if(len(a)!=0):
  a.reverse()
  for j in range(len(a)):
    s+=str(a[j])+" "
  a.clear()
print(s)

  
  




