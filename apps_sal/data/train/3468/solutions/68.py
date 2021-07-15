def scramble(s1, s2):
    s1_counter = [0] * 256
    s2_counter = {}

    for c in s1:
        idx = ord(c)
        s1_counter[idx] += 1

    for c in s2:
        if c in s2_counter:
            s2_counter[c] += 1
        else:
            s2_counter[c] = 1

    for (key, value) in s2_counter.items():
        idx = ord(key)
        if s1_counter[idx] < value:
            return False

    return True
