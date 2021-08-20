n = int(input())
for i in range(2 * n - 1):
    a = n
    if i < n:
        for j in range(2 * n - 1):
            print(a, end=' ')
            if i > j:
                a = a - 1
            elif i + j >= 2 * n - 2:
                a = a + 1
    elif i >= n:
        for j in range(2 * n - 1):
            print(a, end=' ')
            if i + j < 2 * n - 2:
                a = a - 1
            elif j >= i:
                a = a + 1
    print()
