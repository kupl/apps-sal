from collections import namedtuple
Dancer = namedtuple('Dancer', ['category', 'x', 'y', 'idx', 'group'])


def read_dancer(idx):
    (group, pos, time) = [int(x) for x in input().split(' ')]
    (x, y) = (None, None)
    if group == 1:
        (x, y) = (pos, 0)
    else:
        (x, y) = (0, pos)
    return Dancer(time - pos, x, y, idx, group)


(n, w, h) = [int(x) for x in input().split(' ')]
dancers = [read_dancer(idx) for idx in range(n)]
dancers_in = sorted(dancers, key=lambda d: (d.category, -d.group, d.x, -d.y))
dancers_out = sorted(dancers, key=lambda d: (d.category, d.group, d.x, -d.y))
end_pos = [None for _ in range(n)]


def get_end_pos(dancer):
    (x, y) = (None, None)
    if dancer.x == 0:
        (x, y) = (w, dancer.y)
    else:
        (x, y) = (dancer.x, h)
    return (x, y)


for i in range(n):
    end_pos[dancers_in[i].idx] = get_end_pos(dancers_out[i])
for i in range(n):
    print(*end_pos[i])
