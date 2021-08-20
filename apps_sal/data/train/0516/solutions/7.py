for _ in range(int(eval(input()))):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    (x, suffix) = (0, 0)
    for (i, a_i) in enumerate(arr):
        for a_j in arr:
            if a_i > a_j:
                x += 1
        for j in range(i + 1, n):
            if a_i > arr[j]:
                suffix += 1
    ans = x * (k * (k - 1) // 2) + suffix * k
    print(ans)
