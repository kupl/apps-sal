testcases = int(input())
for i in range(testcases):
    n = int(input())
    for i in range(n + 1):
        k = n
        print(' ' * (n - i), end='')
        for j in range(i + 1):
            print(k, end='')
            k -= 1
        print()
    for i in range(n):
        k = n
        print(' ' * (i + 1), end='')
        for j in range(n - i):
            print(k, end='')
            k -= 1
        print()
