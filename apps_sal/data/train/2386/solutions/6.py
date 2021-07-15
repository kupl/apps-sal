for _ in range(int(input())):
    n=int(input())
    x=[int(x) for x in input().split()]
    a=[]
    for i in x:
        if len(a)<n:
            if i not in a:
                a.append(i)
        else:break
    print(*a)

