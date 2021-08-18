for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        if i == 0 or i == 1 or i == n - 1:
            for j in range(i + 1):
                print("*", end='')
        else:
            for j in range(n):
                if j == 0 or j == i:
                    print('*', end='')
                else:
                    print(" ", end='')
        print()
