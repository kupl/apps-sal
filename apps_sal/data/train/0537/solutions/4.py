n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort()
i=0
fin=0
for j in range(0,n):
    while(i<n):
        if(l[i]-l[j]>=k):
            fin=fin+(n-i)
            break
        i=i+1
print(fin)
