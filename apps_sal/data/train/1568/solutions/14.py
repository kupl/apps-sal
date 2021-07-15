# cook your dish here
for i in range(int(input())):
    N=int(input())
    A=[int(x) for x in input().split()]
    P=N/2
    count=0
    for j in range(N):
        if(A[j]>=P):
            count+=1
    print(count)

