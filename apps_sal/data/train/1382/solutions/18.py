#print('hare krishna')
n=int(input())
l=[int(i) for i in input().split()]
x=int(input())
l1=sorted([i for i in l if i<0])
k=sum(i<0 for i in l)
if k<=x:
 print(-sum(i for i in l if i<0))
else:
 # print(l1)
 elem=-(l1[x-1])
 #print(elem)
 ans=elem*x 
 for i in range(x-1):
  ans+=(abs(l1[i])-elem)
 print(ans)

