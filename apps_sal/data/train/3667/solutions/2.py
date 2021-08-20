from collections import deque


def mid_endian(n):
    (h, m) = (hex(n)[2:].upper(), deque())
    if len(h) & 1:
        h = '0' + h
    for i in range(len(h) >> 1):
        if i & 1:
            m.appendleft(h[i << 1:i + 1 << 1])
        else:
            m.append(h[i << 1:i + 1 << 1])
    return ''.join(m)
