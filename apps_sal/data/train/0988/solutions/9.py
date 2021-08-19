tc = int(input())
while tc > 0:
    n = int(input())
    sum = []
    s = 0
    lis = list(map(int, input().split()))
    for i in range(n):
        x = lis[i]
        s = 0
        for j in range(n):
            y = lis[j]
            s += y ^ x
        sum.append(s)
    print(min(sum))
    tc -= 1
