for _ in range(int(input())):
    (n, k, v) = map(int, input().split())
    l = list(map(int, input().split()))
    a = v * (n + k) - sum(l)
    x = a // k
    if x <= 0:
        print('-1')
    elif a % k != 0:
        print('-1')
    else:
        print(x)
