# cook your dish here
import sys

t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    maxx=arr[0]+arr[1]+arr[2]
    summ=maxx
    for i in range(n-3):
        summ=summ-arr[i]+arr[i+3]
        maxx=max(summ,maxx)
    if(arr[-1]+arr[-2]+arr[0]>maxx):
        maxx=arr[-1]+arr[-2]+arr[0]
    print(maxx)
