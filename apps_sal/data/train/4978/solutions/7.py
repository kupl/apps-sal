import re
from collections import deque


def encode(n, s):
    s = s.replace('\n', '`')
    for i in range(n):
        pos, s = get_pos(s), deque(s.replace(' ', ''))
        deque.rotate(s, n)
        s = rotate(set_pos(s, pos), n, 1)
    return str(n) + ' ' + s.replace('`', '\n')


def decode(s):
    n, s = re.search(r'^\d+', s).group(), s.replace('\n', '`')
    s, n = s[len(n) + 1:], int(n)
    for i in range(n):
        pos, s = get_pos(s), deque(''.join(deque(rotate(s, n, -1))).replace(' ', ''))
        deque.rotate(s, -n)
        s = ''.join(set_pos(s, pos))
    return s.replace('`', '\n')


def get_pos(s): return [l for l, j in enumerate(s) if j == ' ']


def rotate(s, n, c):
    li = []
    for k in re.findall(r'(.+?)(\s+)|(.+$)', ''.join(s)):
        t = deque(k[0] or k[-1])
        deque.rotate(t, n * c)
        li.append(''.join(t) + k[1])
    return ''.join(li)


def set_pos(s, position):
    for pos in position:
        s.insert(pos, ' ')
    return s
