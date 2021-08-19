import numpy as np


def six_column_encryption(s):
    s = s.replace(' ', '.') + '.' * int(6 * np.ceil(len(s) / 6) - len(s))
    s = [list(s[i:i + 6]) for i in range(0, len(s), 6)]
    arr = np.array(s).reshape(-1, 6).T
    return ' '.join(map(''.join, arr))
