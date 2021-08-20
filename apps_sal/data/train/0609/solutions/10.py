for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    left = 0
    total_q = 0
    for i in range(n):
        total_q += arr[i]
        total_q = total_q - k if total_q - k > 0 else 0
    left = total_q
    if not left:
        print(n)
    else:
        print(n + int(left / k) + 1)
