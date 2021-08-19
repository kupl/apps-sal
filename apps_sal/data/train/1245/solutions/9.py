try:
    for i in range(int(input())):
        n = int(input())
        s = 1
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                print(s, end='')
                s += 2
            print('\r')
except Exception:
    pass
