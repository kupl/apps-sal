for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    x, suffix = 0, 0
    for i, a_i in enumerate(arr):
        for j, a_j in enumerate(arr):
            if a_i > a_j:
                x += 1
            if j > i:
                if a_i > a_j:
                    suffix += 1
    print(x * ((k * (k - 1)) // 2) + suffix * k)
