buf = [0]


def recaman(n):
    while len(buf) <= n:
        x = buf[-1]
        v = x - len(buf)
        buf.append(v if 0 <= v and v not in buf else x + len(buf))
    return buf[n]
