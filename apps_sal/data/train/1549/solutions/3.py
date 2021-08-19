for _ in range(int(input())):
    n = int(input())
    flag = False
    s = n
    for i in range(2 * n + 1):
        if s >= 0:
            for j in range(s):
                print(' ', end='')
            for j in range(n + 1 - s):
                print(j + s, end='')
        else:
            for j in range(abs(s)):
                print(' ', end='')
            for j in range(n + 1 - abs(s)):
                print(j + abs(s), end='')
        print()
        s -= 1
