for _ in range(int(input())):
    s = list(map(int, list(input())))
    s.append('0')
    y = 0
    if s[0] == 0:
        y = 1
    while s[0] == 0:
        s.remove(0)
    while s[0] == 1:
        s.remove(1)
    z = 0
    while s[0] == 0:
        s.remove(0)
        z += 1
    if y == 1:
        print(0)
    else:
        print(z)

