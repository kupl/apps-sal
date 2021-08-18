for __ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    l = []
    for i in arr:
        if i % k == 0:
            l.append('1')
        else:
            l.append('0')
    print(''.join(l))
