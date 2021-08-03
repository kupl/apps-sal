# cook your dish here

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        if i < (n // 2):
            print(' ' * i, end='')
        else:
            print(' ' * (n - i - 1), end="")

        print("*")
