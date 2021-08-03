for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        for j in range(n):
            print(bin(i * n + j + 1)[2:], end=' ')
        print()
