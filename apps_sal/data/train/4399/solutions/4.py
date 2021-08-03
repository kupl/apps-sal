BASE = {'  x\nxxx\n x \n x ', ' x\n x\nxx\nx \nx ', ' x \n xx\nxx \n x ', 'xx \n xx\n x \n x ', ' x \n xx\nxx \nx  ', 'xxx\n x \n x \n x ', 'xx \n x \n xx\n x ', 'xx \n x \n xx\n  x', 'xx \n x \n x \n xx', '  xx\n xx \nxx  ', ' x \nxxx\n x \n x '}


def reflect(s):
    return '\n'.join(r[::-1] for r in s.split('\n'))


def rotate(s):
    return '\n'.join(''.join(c[::-1]) for c in zip(*s.split('\n')))


def fold_cube(arr):
    table = [[' '] * 5 for _ in range(5)]
    x0, y0, x1, y1 = 4, 4, 0, 0
    for p in arr:
        x, y = divmod(p - 1, 5)
        table[x][y] = 'x'
        x0, y0 = min(x, x0), min(y, y0)
        x1, y1 = max(x, x1), max(y, y1)
    net = '\n'.join(''.join(r[y0:y1 + 1]) for r in table[x0:x1 + 1])
    net2 = reflect(net)
    for i in range(4):
        if net in BASE or net2 in BASE:
            return True
        net, net2 = rotate(net), rotate(net2)
    return False
