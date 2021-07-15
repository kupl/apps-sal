# cook your dish here
for i in range(int(input())):
 a,b=list(map(int,input().split()))
 ls=list(map(int,input().split()))
 ls.sort()
 l1=sum(ls[b:])-sum(ls[:b])
 l2=sum(ls[a-b:])-sum(ls[:a-b])
 print(max(l1,l2))
 

