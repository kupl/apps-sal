for _ in range(int(input())):
    n = int(input())
    p = 0
    for i in range(n):
        p += i + 1
        for j in range(p, p - i - 1, -1):
            print(j, end='')
        print()
