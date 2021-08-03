from collections import Counter
test = int(input())
for _ in range(test):
    s = input()
    c = Counter(s)
    vertical = min(c['U'], c['D'])
    horizontal = min(c['L'], c['R'])
    if vertical == 0 and horizontal == 0:
        print(0)
    elif horizontal == 0:
        print(2)
        print('UD')
    elif vertical == 0:
        print(2)
        print('LR')
    else:
        print(2 * (vertical + horizontal))
        print('L' * horizontal + 'U' * vertical + 'R' * horizontal + 'D' * vertical)
