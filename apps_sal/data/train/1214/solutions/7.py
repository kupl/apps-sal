# code
t = int(input())
c = 1
while t > 0:
    inp = [int(i) for i in input().split(' ')]
    m = inp[0]
    n = inp[1]
    inp = [int(i) for i in input().split(' ')]
    rx = inp[0]
    ry = inp[1]
    path_len = int(input())
    path = input()

    # print(path)
    posx = 0
    posy = 0
    for p in path:
        if p == 'L':
            posx -= 1
        elif p == 'R':
            posx += 1
        elif p == 'U':
            posy += 1
        elif p == 'D':
            posy -= 1

    if posx > m or posx < 0 or posy > n or posy < 0:
        print('Case ' + str(c) + ': ' + 'DANGER')
    elif posx != rx or posy != ry:
        print('Case ' + str(c) + ': ' + 'SOMEWHERE')
    elif posx == rx and posy == ry:
        print('Case ' + str(c) + ': ' + 'REACHED')
    t -= 1
    c += 1
