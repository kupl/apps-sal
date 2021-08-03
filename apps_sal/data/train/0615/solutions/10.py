T = int(input())
while(T != 0):
    n, q = [int(x) for x in input().split(' ')]
    N = [int(x) for x in input().split(' ')]
    while(q != 0):
        s = 0
        x, y = [int(x) for x in input().split(' ')]
        for i in range(x - 1, y):
            s = s + N[i]
        print(s)
        q -= 1
    T -= 1
