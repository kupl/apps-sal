t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    d = ''
    for i in range(n):
        if k[i] % m == 0:
            d += '1'
        else:
            d += '0'
    print(d)
