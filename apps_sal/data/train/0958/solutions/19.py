# cook your dish here
for u in range(int(input())):
    n = int(input())
    for i in range(n):
        for space in range(n - i - 1):
            print(' ', end="")
        for j in range(2 * (i + 1) - 1):
            if j == 0 or j == 2 * i:
                print('*', end="")
            elif i == n - 1:
                print('*', end="")
            else:
                print(' ', end="")
        print()
