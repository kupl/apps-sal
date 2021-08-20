for _ in range(int(input())):
    n = int(input())
    t = n
    s = 0
    for i in range(n):
        for j in range(n - i):
            t -= 1
            s += 1
            print(s, end='')
        print('\r')
