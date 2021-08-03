# cook your dish here
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    c = 1
    d = 0
    for i in w:
        if i > k:
            c = -1
            break
        d += i
        if d > k:
            d = i
            c += 1
    print(c)
