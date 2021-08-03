for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    sum_arr = sum(arr)

    l = [0 for i in range(n)]
    count = 0
    for idx in range(n):
        if arr[idx] >= count + 1:
            count += 1
        else:
            count = arr[idx]
        l[idx] = count

    r = [0 for i in range(n)]
    count = 0
    for idx in range(n - 1, -1, -1):
        if arr[idx] >= count + 1:
            count += 1
        else:
            count = arr[idx]
        r[idx] = count

    optimum = [min(l[i], r[i]) for i in range(n)]
    max_m = max(optimum)

    print(sum_arr - (max_m**2))
