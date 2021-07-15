def solve(n):
    for i in range(1,n+1):
        j=1
        for k in range(1,n+1):
            print(j,end='')
            if j==1:
                j=0
            else:
                j=1
        print()
for _ in range(int(input())):
    n=int(input())
    #s=input()
    #a,b=map(int,input().split())
    #l=list(map(int,input().split()))
    solve(n)

