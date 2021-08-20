t = int(input())
for i in range(t):
    (m, n) = map(int, input().split())
    (rx, ry) = map(int, input().split())
    x = 0
    y = 0
    num = int(input())
    s = input()
    for j in s:
        if j == 'U':
            y = y + 1
        elif j == 'D':
            y = y - 1
        elif j == 'R':
            x = x + 1
        elif j == 'L':
            x = x - 1
    if x == rx and y == ry:
        print('Case ' + str(i + 1) + ': REACHED')
    elif x != rx and y != ry and (x <= m) and (y <= n) and (x > 0) and (y > 0):
        print('Case ' + str(i + 1) + ': SOMEWHERE')
    elif x > m or y > n or x < 0 or (y < 0):
        print('Case ' + str(i + 1) + ': DANGER')
