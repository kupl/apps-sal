n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
count=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if(abs(l[i]-l[j])>=k):
            count=count+1
print(count)
        

