#
n,k = list(map(int,input().split()))
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
min=arr[n-1]
#nt(arr,min)
for i in range(n-k):
    temp=arr[k+i-1]-arr[i]
    #print(temp)
    if temp<min:
        min=temp
print(min)
    

