for _ in range(int(input())):
    n = int(input())
    a = 0
    for _ in range(1, n + 2):
        print('*' * (_ - 1), end="")
        print(_ - 1)
    print()
