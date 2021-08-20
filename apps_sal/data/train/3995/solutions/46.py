import numpy as np


def dating_range(age):
    if age > 14:
        return f'{int(np.floor(age / 2 + 7))}-{int(np.floor((age - 7) * 2))}'
    else:
        return f'{int(np.floor(age - 0.1 * age))}-{int(np.floor(age + 0.1 * age))}'
