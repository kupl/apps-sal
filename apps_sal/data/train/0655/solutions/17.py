for t in range(int(input())):
    (n, k, v) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    v = v * (n + k)
    v = v - sum(l)
    if v > 0 and v % k == 0:
        print(v // k)
    else:
        print('-1')
