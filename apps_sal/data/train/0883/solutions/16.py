for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    c = max(b)
    if a == 1:
        print('-1')
    else:
        l = set(b)
        if b == [c] * a:
            if c == 0:
                print(a)
            elif c == a - 1:
                print('0')
            else:
                print('-1')
        elif len(l) == 2:
            if b.count(c) == a - c and b.count(c - 1) == c:
                print(a - c)
            else:
                print('-1')
        else:
            print('-1')
