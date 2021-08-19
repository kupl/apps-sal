t = int(input())
for j in range(t):
    (n, k) = list(map(int, input().split()))
    s = list(map(int, input().split()))
    sum = 0
    for i in range(0, n - 1, 2):
        if sum >= 0:
            sum += s[i]
        else:
            sum -= s[i]
        if sum >= 0:
            sum -= s[i + 1]
        else:
            sum += s[i + 1]
    if n % 2 != 0:
        if sum <= 0:
            sum -= s[n - 1]
        else:
            sum += s[n - 1]
    if k <= abs(sum):
        print(1)
    else:
        print(2)
