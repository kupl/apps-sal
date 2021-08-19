T = int(input())
for _ in range(T):
    (p1, p2, k) = map(int, input().split())
    num = p1 + p2
    if num % k:
        res = num // k
        if res % 2:
            print('COOK')
        else:
            print('CHEF')
    else:
        res = num // k
        if res % 2:
            print('COOK')
        else:
            print('CHEF')
