n = int(input())
a = list(map(int, input().split()))
q = int(input())
while q > 0:
    i = 1
    tot = a[0]
    b = list(map(int, input().split()))
    if b[0] == 1:
        a[b[1] - 1] = b[2]
    else:
        tot = a[0]
        while 1 + i * b[1] <= n:
            tot = tot * a[i * b[1]]
            i = i + 1
        m = (str)(tot)
        tot = tot % 1000000007
        print((int)(m[0]), tot)
    q = q - 1
