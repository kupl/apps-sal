for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(max(l[0],l[n-1]))
