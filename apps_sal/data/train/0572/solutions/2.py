for i in range(int(input())):
    (a, b, k) = list(map(int, input().split()))
    k1 = abs(a - b)
    if k1 >= k:
        print(k1 - k)
    else:
        print(0)
