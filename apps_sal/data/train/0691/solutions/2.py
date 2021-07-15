# cook your dish here
for t in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 l1=[ ]
 for i in range(len(l)):
  c=0
  for j in range(i):
   if l[j]%l[i]==0:
    c+=1
  l1.append(c)
 print(max(l1))
