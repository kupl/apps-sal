def slove():
    import sys
    import collections
    input = sys.stdin.readline
    n, t = list(map(int, input().rstrip('\n').split()))
    a = list(map(int, input().rstrip('\n').split()))
    b = collections.defaultdict(list)
    m_c = 10 ** 9
    for i, v in enumerate(a):
        if i != 0 and m_c < v:
            b[v-m_c] += [m_c]
        m_c = min(m_c, v)
    b = sorted(list(b.items()), reverse=True)[0]
    print((len(collections.Counter(b[1]))))


def __starting_point():
    slove()

__starting_point()
