for _ in range(int(input())):
    n = int(input())
    s = [str(i) for i in range(n, 0, -1)]
    for i in range(n):
        print('*' * i + ''.join(s))
        del(s[0])
