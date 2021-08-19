for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('0')
    else:
        s = []
        for i in range(n):
            s.append(str(i))
        print(''.join(s))
        p = 1
        for i in range(n - 1):
            s.pop(n - 1)
            s = [str(p)] + s
            print(''.join(s))
            p += 1
