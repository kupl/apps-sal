from itertools import combinations
def rSubset(arr, r):  
    return list(combinations(arr, r))
arr=[]
arr=list(map(int,input().split()))
N,T=arr[0],arr[1]
arr.remove(N)
arr.remove(T)
arr=rSubset(arr,4)
sum=0
for i in range(0,len(arr)):
    a=list(arr[i])
    if a[0]+a[1]+a[2]+a[3]==T:
        sum+=1
print(sum)        
