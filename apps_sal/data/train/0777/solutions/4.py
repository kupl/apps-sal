for i in range(eval(input())):
    (r1, h1, r2, h2) = list(map(float, input().split()))
    a = 3.141592653589793 * r1 ** 2 * h1 / 3 + 2 * 3.141592653589793 * r1 ** 3 / 3
    b = 3.141592653589793 * r2 ** 2 * h2
    print('%.9f' % a, '%.9f' % b)
