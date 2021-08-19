t = int(input().strip())
for j in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    x = 1
    while x < n + 1:
        if arr[x] > arr[0]:
            break
        x = x + 1
    if x == n + 1:
        print(0)
    else:
        print(n - x + 1)
