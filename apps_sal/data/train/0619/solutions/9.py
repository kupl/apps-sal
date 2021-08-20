for _ in range(int(input())):
    (a, b, k) = map(int, input().split())
    c = a + b
    d = c // k
    if d % 2 == 0:
        print('CHEF')
    elif d % 2 != 0:
        print('COOK')
