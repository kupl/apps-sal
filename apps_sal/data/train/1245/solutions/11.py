def solve(n):
    j = 1
    for i in range(1, n + 1):
        for k in range(n):
            print(j, end='')
            j += 2
        print()


for _ in range(int(input())):
    n = int(input())
    # s=input()
    # a,b=map(int,input().split())
    # l=list(map(int,input().split()))
    solve(n)
