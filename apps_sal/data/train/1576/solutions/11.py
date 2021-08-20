t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i + j + 1 <= n:
                print(i + j + 1, end='')
            else:
                print(i + j - n + 1, end='')
        print()
