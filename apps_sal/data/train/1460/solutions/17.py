try:
    num = list(map(int, input().split()))
    n = num[0]
    x = num[1]
    y = num[2]
    inp = list(map(int, input().split()))
    x = x * n
    dic = {}
    dic[1] = y
    for i in range(2, n + 1):
        dic[i] = y - 0.02 * y
        y = dic[i]
    for i in inp:
        x += dic[i]
    if x < 300:
        print('NO')
    else:
        print('YES')
except EOFError:
    pass
