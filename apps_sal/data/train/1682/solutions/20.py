import math
n=int(input())
s=str(n)
arr=list()
for ss in s:
    arr.append(int(ss))
nn=len(arr)
maxi=0
first=0
last=0
for i in range(nn):
    mm=arr[i]
    sum=arr[i]
    f=i+1
    l=i+1
    for j in range(i+1,nn):
        if arr[j]>mm:
            mm=arr[j]
            sum+=arr[j]
            l=j+1
    if sum>maxi:
        maxi=sum
        first=f
        last=l
print(f'{maxi}:{first}-{last}')



    

    


