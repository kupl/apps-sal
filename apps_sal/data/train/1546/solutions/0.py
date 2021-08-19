def check(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 'NO'
    else:
        i = 3
        while i > 0:
            if a * a == b * b + c * c:
                return 'YES'
            else:
                t = a
                a = b
                b = c
                c = t
                i -= 1
    return 'NO'


try:
    for _ in range(int(input())):
        (a, b, c) = map(int, input().split())
        print(check(a, b, c))
except:
    print(e)
    pass
