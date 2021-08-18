for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = input().split()

    head_count = 0

    for i in range(n - 1, n - k - 1, -1):
        if arr[i] == "H":
            if head_count % 2 == 0:
                head_count += 1
        else:
            if head_count % 2 != 0:
                head_count += 1

    if head_count % 2 == 0:
        print(arr[:n - k].count("H"))
    else:
        print(arr[:n - k].count("T"))
