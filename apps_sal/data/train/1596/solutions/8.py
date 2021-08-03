for _ in range(int(input())):
    x, y = map(int, input().split())
    x = (bin(x + 1)[2:]).count('1')
    y = (bin(y + 1)[2:]).count('1')

    if x == y:
        print(0, 0)
    elif x < y:
        print(1, abs(x - y))
    else:
        print(2, abs(x - y))
