# cook your dish here
for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    A.sort()
    for i in range(len(A)):
        if A[i]==1:
            print(i)
            break
