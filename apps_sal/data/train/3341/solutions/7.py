def pop_shift(strn):
    s2 = ''.join((strn[-i - 1] for i in range(len(strn) // 2)))
    s1 = ''.join((strn[i] for i in range(len(strn) // 2)))
    s0 = ''.join(strn[len(s1):-len(s1)])
    if len(strn) == 1:
        s0 = strn
    return [s2, s1, s0]
