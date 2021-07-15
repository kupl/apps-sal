# cook your dish here
t=int(input())
for i in range(0,t):
    n,m=list(map(int,input().split()))
    list1=[]
    arr1=list(map(int,input().split()))[:n]
    arr2=list(map(int,input().split()))[:m]
    res = list(set(arr2)^set(arr1))
    print(*res)

