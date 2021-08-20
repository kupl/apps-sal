for _ in range(int(input())):
    (x, y) = list(map(int, input().split()))
    if y - x == 0:
        print(0)
        continue
    if y - x > 0:
        if (y - x) % 2:
            print(1)
            continue
        if not (y - x) % 2 and (y - x) % 4:
            print(2)
            continue
        else:
            print(3)
            continue
    if y - x < 0:
        if (y - x) % 2:
            print(2)
            continue
        else:
            print(1)
            continue
