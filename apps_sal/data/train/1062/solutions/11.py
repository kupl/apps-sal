n = int(input())
for i in range(n, 0, -1):
    k = n
    j = 1
    while j <= 2 * n - 1:
        print(k, end=' ')
        j += 1
        if i < k:
            k -= 1
        if i == k:
            for l in range(2 * k - 1):
                if j > 2 * n - 1:
                    break
                print(k, end=' ')
                j += 1
            k += 1
            while k != i:
                if j > 2 * n - 1:
                    break
                print(k, end=' ')
                k += 1
                j += 1
    print()
for i in range(2, n + 1):
    k = n
    j = 1
    while j <= 2 * n - 1:
        print(k, end=' ')
        j += 1
        if i < k:
            k -= 1
        if i == k:
            for l in range(2 * k - 1):
                if j > 2 * n - 1:
                    break
                print(k, end=' ')
                j += 1
            k += 1
            while k != i:
                if j > 2 * n - 1:
                    break
                print(k, end=' ')
                k += 1
                j += 1
    print()
