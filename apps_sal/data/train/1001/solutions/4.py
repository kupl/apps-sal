# cook your dish here
t=int(input())
for _ in range(t):
 n=int(input())
 l=list(map(int,input().split()))[:n]
 count=1
 for i in range(1,n):
  li=[]
  for j in range(6):
   if (i-j)<0:
    break
   else:
    li.append(l[i-j])
  #print(li)
  li.sort()
  #print(li)
  if l[i]==li[0] and li[0]!=li[1]:
   count+=1
 print(count)

