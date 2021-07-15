# cook your dish here
T = int(input())

for i in range(T):
    N,dataA,dataB = int(input()),list(map(int,input().split())),list(map(int,input().split()))
    if(max(dataA)!=max(dataB)):
        print("YES")
    else:
        print("NO")
