for i in range(int(input())):
    n = int(input())

    for j in range(0, n):
        s = ""
        for k in range(1, n + 1):
            p = n * j + k
            s += str(2 * p - 1)
        print(s)
