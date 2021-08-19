for _ in range(0, int(input())):
    a = int(input())
    for i in range(1, a ** 2 * 2, a * 2):
        for j in range(i, a * 2 + i, 2):
            print(j, end='')
        print()
