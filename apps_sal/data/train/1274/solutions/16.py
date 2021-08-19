for a0 in range(int(input())):
    n = int(input())
    for j in range(1, n + 1):
        s = ''
        for i in range(1, n + 1):
            s += str(i) + str(j)
        print(s)
