t = int(input())
while t > 0:
    n = int(input())
    a = [int(ele) for ele in input().split()]
    for i in range(n):
        num = bin(a[i])
        if num[-1] == '1':
            a[i] = 1
        else:
            a[i] = 0
        if i != 0:
            a[i] += a[i - 1]
    q = int(input())
    while q > 0:
        l, r = [int(ele) for ele in input().split()]
        x = a[r - 1]
        if l == 1:
            y = 0
        else:
            y = a[l - 2]
        if (x - y == (r - l + 1)):
            print("ODD")
        else:
            print("EVEN")
        q -= 1
    t -= 1
