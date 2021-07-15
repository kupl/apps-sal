N,M,K=list(map(int,input().split()))
s=0
certi=0
for i in range(N):
 l=[]
 l=list(map(int,input().split()))
 s=sum(l)-l[-1]
 if s>=M and l[-1]<=10:
  certi+=1

 
print(certi)# cook your dish here

