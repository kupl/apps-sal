def shorter_reverse_longer(a, b):

    def s_r_l(s, l):
        return s + l[::-1] + s
    assert isinstance(a, str) and isinstance(b, str), 'Both arguments must be strings'
    if len(b) > len(a):
        return s_r_l(a, b)
    else:
        return s_r_l(b, a)
