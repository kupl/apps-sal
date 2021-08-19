for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    left = 0
    total_q = 0
    flag = 0
    for i in range(n):
        total_q += arr[i]
        if total_q < k:
            flag = 1
            break
        total_q = total_q - k
    left = total_q
    if flag:
        print(i + 1)
    elif not left:
        print(n)
    else:
        print(n + int(left / k) + 1)
