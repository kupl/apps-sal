for _ in range(int(input())):
    n=int(input())
    l=[i for i in range(1,n+1)]
    for i in range(n):
        if l[i]==i+1:
            try:
                l[i],l[i+1]=l[i+1],l[i]
            except:
                l[i],l[i-1]=l[i-1],l[i]
    for item in l:
        print(item,end=" ")
    print()
