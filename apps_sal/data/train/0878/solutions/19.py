for i in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    a = 0
    c = []
    b = []
    for i in range(n):
        m = arr[i] - a
        if(k >= m):
            pass
        else:

            if m % k == 0:
                c.append(int(m / k) - 1)

            else:
                b.append(int(m / k))

        a = arr[i]
    print(sum(c) + sum(b))
