# cook your dish here
import math
for _ in range(int(input())):
    N=int(input())
    arr=[]
    for i in range(1,N+1):
        arr.append(math.pow(i,3))
    for i in range(1,N):
        arr.append(math.pow(i,3))
    print(int(sum(arr)))
