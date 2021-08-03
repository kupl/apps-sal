t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        for j in range(2 * n):
            if j % 2 == 0:
                print(int(j / 2) + 1, end='')
            else:
                print(i + 1, end='')
        print()
