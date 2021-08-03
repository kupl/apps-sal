from collections import defaultdict


def poohbear(s):
    C, k, p, copy, r = defaultdict(int), 0, 0, 0, ''
    while p < len(s):
        if s[p] == 'W' and C[k] == 0:
            p = s.index('E', p)
        elif s[p] == 'E' and C[k]:
            p = p - s[:p][::-1].index('W') - 1
        elif s[p] == '>':
            k += 1
        elif s[p] == '<':
            k -= 1
        elif s[p] == 'P':
            r += chr(C[k])
        elif s[p] == 'N':
            r += str(C[k])
        elif s[p] == 'c':
            copy = C[k]
        else:
            C[k] = {'+': C[k] + 1, '-': C[k] - 1, 'L': C[k] + 2, 'I': C[k] - 2, 'V': C[k] / 2, 'T': C[k] * 2,
                    'A': C[k] + copy, 'B': C[k] - copy, 'Y': C[k] * copy, 'D': C[k] / max(copy, 1), 'p': copy,
                    'U': C[k]**0.5, 'Q': C[k]**2}.get(s[p], C[k])
            C[k] = int(C[k] // 1) % 256
        p += 1
    return r
