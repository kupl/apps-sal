n,k=list(map(int,input().strip().split()))
a=list(map(int,input().strip().split()))
s=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if abs(a[i]-a[j])>=k:
            s+=1
    
print(s)

