for _ in range(int(input())):
    n=int(input())
    c=0
    l=list(map(int,input().split()))
    for i in range(len(l)):
        if(l[i]%2==0):
            c+=l[i]
    print(c)

