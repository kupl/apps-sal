n = int(input())
val = (2 * n) - 1
x = 2

for i in range(val):
    k = n + 1
    h = -1
    count = 0
    for j in range(val):
        if i < n:
            if h < i:
                h += 1
                k -= 1
                print(k, end=' ')
                if h == i:
                    count = 1
                    val1 = (2 * k) - 1

            elif (count > 0) and (count < val1):
                count += 1
                print(k, end=' ')

            else:
                k += 1
                print(k, end=' ')

        else:
            if (h < i) and (k != x) and (count == 0):
                h += 1
                k -= 1
                print(k, end=' ')
                if k == x:
                    count = 1
                    val1 = (2 * x) - 1

            elif count < val1:
                count += 1
                print(k, end=' ')

            else:
                k += 1
                print(k, end=' ')

    if i >= n:
        x += 1
    print()
