for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in list(map(int,input().split())):
        if i >= n//2:
            c+=1
    print(c)


