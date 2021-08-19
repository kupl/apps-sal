# cook your dish here
t = int(input())
while t:
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    z = []
    for i in d:
        if d[i] > k:
            z.append(i)
    z.sort()
    print(*z)
    t -= 1
