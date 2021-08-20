for i in range(int(input())):
    n = int(input())
    for j in range(0, n):
        s = ''
        for k in range(1, n + 1):
            s += str(j + k + 1)
        print(s)
