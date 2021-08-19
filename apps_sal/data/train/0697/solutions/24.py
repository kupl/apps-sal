t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    test = sum((a[i] for i in range(k)))
    win = test
    for i in range(k, n):
        test = test - a[i - k] + a[i]
        if test > win:
            win = test
    print(win)
