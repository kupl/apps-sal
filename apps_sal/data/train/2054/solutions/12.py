import collections
import sys


def read_ints():
    return [int(x) for x in sys.stdin.readline().strip().split()]


def main():
    N = read_ints()[0]
    edges = []
    vx_to_neighbor_colors = collections.defaultdict(set) 
    for _ in range(N - 1):
        u, v = read_ints()
        u -= 1
        v -= 1
        edges.append((u, v))
    colors = read_ints()

    vx_to_cnt = collections.Counter()
    e_cnt = 0
    for e in edges:
        if colors[e[0]] == colors[e[1]]:
            continue
        vx_to_cnt[e[0]] += 1
        vx_to_cnt[e[1]] += 1
        e_cnt += 1

    if e_cnt == 0:
        return 1  # any
    if e_cnt == 1:
        return 1 + list(vx_to_cnt.keys())[0]

    root = None
    for vx, cnt in list(vx_to_cnt.items()):
        if cnt == e_cnt:
            if root is not None:
                return None
            root = 1 + vx
        elif cnt != 1:
            return None
    return root


def __starting_point():
    root = main()
    if root is not None:
        print(f'YES\n{root}')
    else:
        print('NO')

__starting_point()
