for _ in range (int(input())):
 n=int(input())
 a1=input()
 b1=input()
 a=[]
 b=[]
 for i in a1:
  a.append(ord(i)-97)
 for i in b1:
  b.append(ord(i)-97)
 ind = [-1]*26
 for i in range (n):
  ind[a[i]]=i
 ans=[]
 temp = 0
 for i in range(n):
  if b[i]>a[i]:
   temp = 1
   break
 for i in range (n):
  if ind[b[i]]==-1:
   temp = 1
 for i in range (24,-1,-1):
  ans.append([])
  ans[-1].append(ind[i])
  for j in range (n):
   if a[j]>i and b[j]==i and ind[i]!=-1:
    ans[-1].append(j)
  if temp == 1:
   break
 if temp == 1:
  print(-1)
 else:
  l = 0
  for i in ans:
   if len(i)!=1:
    l+=1
  print(l)
  for i in ans:
   if len(i)!=1:
    print(len(i),end=" ")
    print(*i)

