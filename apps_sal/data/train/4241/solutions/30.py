def sequence_sum(b, e, s):
    return (lambda a: a * (a + 1) / 2 * s + b * (a + 1))(int((e - b) / s)) if b <= e else 0
