for _ in range(eval(input())):
    n = eval(input())
    [m, f] = list(map(int, input().split()))
    s = list(map(int, input().split()))
    mc = fc = 0
    for i in s:
        if i > 0 and i % m == 0:
            mc += 1
        elif i > 0 and i % f == 0:
            fc += 1
    total = mc + fc
    if total < 0.7 * n:
        print('No')
    else:
        print('Yes')
        if mc == fc:
            print('Both')
        elif mc > fc:
            print('Multan')
        else:
            print('Fultan')
