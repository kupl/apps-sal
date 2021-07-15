for _ in range(int(input())):
    c=0
    n = int(input())
    w = [int(x) for x in input().split()]
    for i in range(n):
        if w[i]>=n/2:
            c=c+1
    print(c)

