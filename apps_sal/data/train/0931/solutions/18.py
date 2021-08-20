def LSB(num, K):
    return bool(num & 1 << K - 1)


for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    c = 0
    for j in a:
        if not LSB(j, 1):
            c += j
    print(c)
