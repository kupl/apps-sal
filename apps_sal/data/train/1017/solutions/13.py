for _ in range(int(input())):
    arr = list(map(int, input().split()))

    summ = sum(arr[: -1])
    if arr[-1] * summ > 120:
        print("Yes")
    else:
        print("No")

    # cook your dish here
