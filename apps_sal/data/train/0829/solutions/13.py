# cook your dish here
n=int(input())
strength=list(map(int,input().split()))
revenue=0
for i in range(0,n-1):
    for j in range(i+1,n):
        x=strength[i]-strength[j]
        if x<0:
            x=0-x
        revenue+=x
print(revenue)
