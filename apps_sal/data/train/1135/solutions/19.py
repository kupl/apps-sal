t=int(input())
for i in range(t):
 n,k=list(map(int,input().split()))
 list1=[i for i in range(1,n)]
 list2=[]
 for i in range(1,k+1):
  list2.append(i)
  list1.remove(i)
 list2.append(n)
 for i in list1:
  list2.append(i)
 print(*list2)
 

