for _ in range(int(input())):
    n=int(input())
    l=[int(j) for j in input().split()]
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    print(*l1)

