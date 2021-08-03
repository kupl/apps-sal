def sequence_sum(b, e, s):
    k = (e - b) // s
    return (1 + k) * (b + s * k / 2) if b <= e else 0
