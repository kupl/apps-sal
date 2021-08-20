for _ in range(int(input())):
    (p1, p2, k) = map(int, input().split())
    x = (p1 + p2) // k
    if x % 2 == 0:
        print('CHEF')
    else:
        print('COOK')
