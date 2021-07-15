# cook your dish here
n=int(input())
s=0
for i in range(n):
    l=list(map(int,input().split()))
    k=l[1]+1-l[0]
    if(l[0]<0 and l[1]<0):
        k=l[0]-l[1]-1
    s+=abs(k)
m=10**9
m+=7
print(s%m)

