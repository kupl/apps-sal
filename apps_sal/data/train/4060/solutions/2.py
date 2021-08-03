def ant_bridge(ants, s):
    remain, i = list(ants), 0

    while True:
        next_stop = next((k for k, l in enumerate(s[i:-1], i) if s[k + 1] == '.'), None)

        if next_stop is None:
            return ''.join(remain)

        if next_stop != i or not i:
            remain.insert(0, remain.pop())
        i = next_stop + 1

        while s[i] == '.':
            remain.insert(0, remain.pop())
            i += 1
        remain.insert(0, remain.pop())
