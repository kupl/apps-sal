for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    for i in range(n-1):
        if l[i] != l[i+1]:
            print(i+1)
