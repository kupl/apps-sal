for t in range(int(input())):
    n, k, v = map(int, input().split())
    a = list(map(int, input().split()))
    b = sum(a)
    x = (v * (n + k) - b) / k
    if int(x) == x and x > 0:
        print(int(x))
    else:
        print('-1')
