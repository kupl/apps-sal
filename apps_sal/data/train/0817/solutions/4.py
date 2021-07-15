for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in l:
        s^=i
    print(s)
