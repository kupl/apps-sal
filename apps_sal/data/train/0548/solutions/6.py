for tc in range(int(input())):
    K = int(input())
    mx = 2 * K - 1
    for i in range(K):
        s = '*' * (2 * i + 1)
        s = ' ' * (mx - len(s) >> 1) + s
        print(s)
        print(s)
