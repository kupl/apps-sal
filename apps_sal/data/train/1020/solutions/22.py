t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            if sum > 0:
                sum += a[i]
            else:
                sum -= a[i]
        else:
            if sum > 0:
                sum -= a[i]
            else:
                sum += a[i]
    if abs(sum) >= k:
        print(1)
    else:
        print(2)
