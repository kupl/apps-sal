for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    r=(max(l)-min(l))+2*k
    print(r)
