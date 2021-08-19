def count_adjacent_pairs(st):
    (s, one, two, c) = (st.lower().split(' '), None, None, 0)
    for w in s:
        c += w == one and w != two
        two = one
        one = w
    return c
