for _ in range(int(input())):
    n,m=map(int,input().split())
    x=[]
    l=set(map(int,input().split()))
    l2=set(map(int,input().split()))
    for i in l:
        if i not in l2:
            x.append(i)
    for i in l2:
        if i not in l:
            x.append(i)
    x.sort()
    for i in x:
        print(i,end=' ')
    print()
