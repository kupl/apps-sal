try:
    for test in range(int(input())):
        k = int(input())
        for i in range(k, 0, -1):
            for j in range(i):
                print(' ', end='')
            for j in range(k, i - 1, -1):
                print(j, end='')
            print()
        for i in range(k + 1):
            for j in range(i):
                print(' ', end='')
            for j in range(k, i - 1, -1):
                print(j, end='')
            print()
except:
    pass
