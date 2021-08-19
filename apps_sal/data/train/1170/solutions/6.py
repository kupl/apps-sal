for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    d = list(map(int, input().split()))
    t = ''
    for i in range(n):
        if d[i] % k == 0:
            t += '1'
        else:
            t += '0'
    print(t)
