for _ in range(int(input())):
    (n, k) = map(int, input().split())
    s = input()
    (a, b) = ([0], [0])
    x = y = 0
    for i in s:
        if i == 'U':
            x -= 1
            a.append(x)
        elif i == 'D':
            x += 1
            a.append(x)
        elif i == 'L':
            y -= 1
            b.append(y)
        elif i == 'R':
            y += 1
            b.append(y)
    row = max(a) - min(a) + 1
    col = max(b) - min(b) + 1
    if row > n or col > k:
        print('unsafe')
    else:
        print('safe')
