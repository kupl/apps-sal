t = eval(input())
while t != 0:
    t -= 1
    n = eval(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    diff = a[0]
    for i in range(1, n):
        if a[i] - a[i - 1] < diff and a[i] - a[i - 1] > 0:
            diff = a[i] - a[i - 1]
    print(diff * n)
