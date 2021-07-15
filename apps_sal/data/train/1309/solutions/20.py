for _ in range(int(input())):
    n = int(input())
    for i in range(n, 0, -1):
        print('*' * (n - i), end = '')
        for j in range(i, 0, -1): print(j, end = '')
        print()
