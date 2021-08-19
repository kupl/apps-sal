for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = ''
    for i in a:
        if i % k == 0:
            s += '1'
        else:
            s += '0'
    print(s)
