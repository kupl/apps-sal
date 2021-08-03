for _ in range(int(input())):
    a, o, g = map(int, input().split())
    while g > 0:
        if a < o:
            a += 1
            g -= 1
        elif o < a:
            o += 1
            g -= 1
        else:
            break
    print(abs(a - o))
