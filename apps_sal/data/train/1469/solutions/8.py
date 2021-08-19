try:
    for i in range(int(input())):
        n = int(input())
        for j in range(1, n + 1):
            s = j + 1
            for k in range(1, n + 1):
                print(s, end='')
                s += 1
            print('\r')
except Exception:
    pass
