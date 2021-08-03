from itertools import groupby


def send(s):
    s = ''.join(format(o, '07b') for o in map(ord, s))
    return ' '.join(
        f"{'0' if key == '1' else '00'} {'0' * sum(1 for _ in grp)}"
        for key, grp in groupby(s)
    )


def receive(s):
    it = iter(s.split())
    xs = ''.join(('1' if c == '0' else '0') * len(n) for c, n in zip(it, it))
    return ''.join(chr(int(xs[i:i + 7], 2)) for i in range(0, len(xs), 7))
