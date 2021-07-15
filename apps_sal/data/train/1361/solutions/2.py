m=list(map(int,input().strip().split()))[:2]
n,k=m
lst=list(map(int,input().strip().split()))[:n]

h=0
while k!=0:
    sum=0
    for i in range(n):
        i=i+h

        sum+=lst[i]
        lst.append(sum)
    k-=1
    h+=n
M = 1000000007
# print(lst)
for j in range (len(lst)-n,len(lst)):
    
    print(lst[j]%M,end=" ")
    
