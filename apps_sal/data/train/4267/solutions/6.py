d = {'warrior': [4, [11, 8, 12, 13, 13, 11, 9, 9]], 'knight': [5, [14, 10, 10, 11, 11, 10, 9, 11]], 'wanderer': [3, [10, 11, 10, 10, 14, 12, 11, 8]], 'thief': [5, [9, 11, 9, 9, 15, 10, 12, 11]], 'bandit': [4, [12, 8, 14, 14, 9, 11, 8, 10]], 'hunter': [4, [11, 9, 11, 12, 14, 11, 9, 9]], 'sorcerer': [3, [8, 15, 8, 9, 11, 8, 15, 8]], 'pyromancer': [1, [10, 12, 11, 12, 9, 12, 10, 8]], 'cleric': [2, [11, 11, 9, 12, 8, 11, 8, 14]], 'deprived': [6, [11, 11, 11, 11, 11, 11, 11, 11]]}


def souls(character, build):
    l = d[character][0]
    p = sum(d[character][1])
    ap = sum(build)
    al = l + ap - p
    s = 0
    for i in range(l + 1, al + 1):
        if i <= 8:
            s = s + 673 + 17 * (i - 2)
        elif i <= 11:
            s = s + 775 + 18 * (i - 8)
        else:
            s = s + round(pow(i, 3) * 0.02 + pow(i, 2) * 3.06 + 105.6 * i - 895)
    return 'Starting as a {}, level {} will require {} souls.'.format(character, al, s)
