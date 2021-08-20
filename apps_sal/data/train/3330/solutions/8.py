import numpy as np


def make_triangle(m, n):
    num = n - m + 1
    level = int((num * 2) ** (1.0 / 2))
    if level * (level + 1) / 2 != num:
        return ''
    else:
        level_max = level * 2 - 1
        npres = np.full((level, level_max), ' ')
        (l, p, f) = (0, level_max // 2, int(str(m)[-1]))
        for i in range(num):
            npres[l][p] = f
            f = (f + 1) % 10
            if p >= level_max // 2 and l != level - 1:
                if npres[l + 1][p + 1] == ' ':
                    l += 1
                    p += 1
                else:
                    p -= 2
                    level -= 1
            elif l == level - 1 and p > 0:
                if npres[l][p - 2] == ' ':
                    p -= 2
                else:
                    p += 1
                    l -= 1
            elif p < level_max // 2 and l != level - 1 or (l == level - 1 and p == 0):
                if npres[l - 1][p + 1] == ' ':
                    p += 1
                    l -= 1
                else:
                    l += 1
                    p += 1
        res = '\n'.join((''.join((str(x) for x in n)).rstrip() for n in npres.tolist()))
        return res
