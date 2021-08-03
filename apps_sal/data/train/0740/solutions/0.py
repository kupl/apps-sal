t = int(input())
while(t):
    t -= 1
    d = {}
    n, m, k = [int(x) for x in list(input().split())]
    sum = 0
    while(k):
        k -= 1
        x, y = [int(x) for x in list(input().split())]
        a = [-1, 1, 0, 0]
        b = [0, 0, -1, 1]
        for i in range(4):
            if((x + a[i], y + b[i]) in d):
                sum -= 1
            else:
                sum += 1
        d[(x, y)] = 1
    print(sum)
