t = int(input())
for i in range(t):
    n = int(input())
    for i in range(1, n + 1):
        str1 = ''
        print(' ' * (n - i), end='')
        if i % 2 == 1:
            for j in range(1, i + 1):
                str1 = str1 + chr(64 + j)
            print(str1)
        else:
            for i in range(1, i + 1):
                print(i, end='')
            print()
