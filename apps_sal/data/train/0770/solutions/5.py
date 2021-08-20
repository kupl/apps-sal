t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().strip().split()))
    ar = list(map(int, input().strip().split()))
    even = []
    odd = []
    for i in range(n):
        if ar[i] % 2 == 0:
            even.append(ar[i])
            odd.append(0)
        else:
            even.append(0)
            odd.append(ar[i])
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = even[0]
    dp2[0] = odd[0]
    for i in range(1, n):
        if i < k + 1:
            dp1[i] = max(dp1[i - 1], even[i])
        else:
            dp1[i] = max(dp1[i - 1], dp1[i - k - 1] + even[i])
    for i in range(1, n):
        if i < k + 1:
            dp2[i] = max(dp2[i - 1], odd[i])
        else:
            dp2[i] = max(dp2[i - 1], dp2[i - k - 1] + odd[i])
    print(dp1[-1] + dp2[-1])
