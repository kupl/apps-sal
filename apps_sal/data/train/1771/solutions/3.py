def closure_gen(*s):
    print(s)
    # Special cases:
    if s == ():
        return
    if s == (1,):
        yield 1
        return
    if len(s) == 1:
        v0, vi = s[0], s[0]
        while True:
            yield vi
            vi *= v0
    s = list(s)
    for i in [0, 1]:
        if i in s:
            yield i
            s.remove(i)

    # === Main ====
    queue = [1]
    seen = set(queue)

    def next_value(i, si, rank):
        while True:
            val = queue[rank] * si
            if val in seen:
                rank += 1
                continue
            break
        seen.add(val)
        return val, i, si, rank

    queues = [next_value(i, si, 0) for i, si in enumerate(s)]

    while True:
        vn, i, si, rank = min(queues)
        queue.append(vn)
        yield vn
        queues[i] = next_value(i, si, rank + 1)
