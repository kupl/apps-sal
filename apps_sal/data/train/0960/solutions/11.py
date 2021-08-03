for no in range(int(input())):
    n = int(input())
    a = 1
    for i in range(n):
        for j in range(n):
            print(bin(a)[2:], end=' ')
            a += 1
        print()
