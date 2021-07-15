def tops(msg):
    if msg:
        step = int(((2 * len(msg) - 1)**0.5 + 3) / 2)
        result = [msg[n*(2*n+1)-1:2*n*(n+1)] for n in range(1, step)]
        return "".join(reversed(result))
    return ""

