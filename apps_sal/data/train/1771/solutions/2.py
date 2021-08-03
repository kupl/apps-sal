def closure_gen(*s):
    if not s:
        return
    if s[0] == 1:
        yield 1
        s = s[1:]
        if not s:
            return
    indices = {x: 0 for x in s}
    seq = [1]
    while True:
        m = float('inf')
        for x, i in indices.items():
            m = min(m, seq[i] * x)
        yield m
        seq.append(m)
        for x, i in indices.items():
            if seq[i] * x == m:
                indices[x] += 1
