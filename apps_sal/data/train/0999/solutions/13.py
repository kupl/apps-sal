try:
    for _ in range(int(input())):
        n = int(input())
        k = n - 1
        c = 65
        num = 1
        for i in range(0, n):
            for j in range(0, k):
                print(end=' ')
            k = k - 1
            for j in range(0, i + 1):
                if i % 2 == 0:
                    print(chr(c + j), end='')
                else:
                    print(num + j, end='')
            print('\r')
except:
    pass
