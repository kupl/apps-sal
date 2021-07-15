# cook your dish here
for _ in range(int(input())):
    n = int(input())
    can = list(map(int, input().split()))
    s = sum(can)
    if(s%n == 0):
        dist = s//n
        op = 0
        for i in range(n):
            if(can[i]>dist):
                op += (can[i] - dist)
        print(op)
    else:
        op = (n - (s%n))
        dist = (s//n)+1
        for i in range(n):
            if(can[i]>dist):
                op += (can[i] - dist)
        print(op)
