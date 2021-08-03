from itertools import cycle


def justify(s, n):
    m, s, final, i = [], s.split(), [], 0
    while i < len(s):
        e = s[i]
        if len(' '.join(final)) + len(e) + 1 <= n:
            final.append(e)
            i += 1
        else:
            final = "  ".join(final).split(' ')
            if len(final) == 1:
                m.append(final[0])
            else:
                nex = cycle(range(1, len(final), 2))
                while len(''.join(final)) < n:
                    final[next(nex)] += ' '
                m.append(''.join(final))
            final = []
    return '\n'.join(m + [' '.join(final)])
