t = int(input())
for i in range(t):
    n = int(input())
    k = int(input())
    a = k % n
    if n % 2 == 0:
        if a > n // 2:
            a = n - a
            print(2 * a)
        elif a < n // 2:
            print(2 * a)
        else:
            print(2 * a - 1)
    elif a > n // 2:
        a = n - a
        print(2 * a)
    else:
        print(2 * a)
