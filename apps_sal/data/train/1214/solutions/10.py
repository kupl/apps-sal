for f in range(int(input())):
    (m, n) = list(map(int, input().split()))
    (rx, ry) = list(map(int, input().split()))
    l = int(input())
    s = input()
    x = 0
    y = 0
    for i in s:
        if i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
        elif i == 'R':
            x += 1
        else:
            x -= 1
    if x < 0 or y < 0 or x > m or (y > n):
        print('Case', str(f + 1) + ':', 'DANGER')
    elif x == rx and y == ry:
        print('Case', str(f + 1) + ':', 'REACHED')
    else:
        print('Case', str(f + 1) + ':', 'SOMEWHERE')
