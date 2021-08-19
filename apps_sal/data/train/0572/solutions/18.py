for _ in range(int(input())):
    (a, b, k) = list(map(int, input().split()))
    if max(a, b) - min(a, b) - k <= 0:
        print('0')
    else:
        print(max(a, b) - min(a, b) - k)
