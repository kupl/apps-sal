import re
import numpy as np

R = np.array([[0, -1], [1, 0]])
d = {'R': R @ R, 'L': R @ R, 'r': R, 'l': -R}
direction = np.array([1, 0])
point = np.zeros(2, 'int')


def i_am_here(path):
    nonlocal direction, point
    for command in re.findall(r'(\d+|[RrLl])', path):
        if command.isdigit():
            point -= direction * int(command)
        else:
            direction = direction @ d[command]
    return list(point)
