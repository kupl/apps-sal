

t = int(input())
while t:
    n = int(input())
    ans = ""
    c = []
    zero = 0
    while n:
        a, b = input().split()
        a = int(a)
        b = int(b)
        if b == 0:
            zero += 1
        if b == 1:
            c.append(repr(a))
        elif b != 0:
            c.append(repr(a * b) + 'x^' + repr((b - 1)))
        n -= 1
    l = len(c)

    if l == 0:
        print(0)
    else:
        cnt = 0
        for i in c:
            print(i, end=' ')
            cnt += 1
            if cnt != l:
                print(' + ', end=' ')
        print('\n', end=' ')
    t -= 1
