def sequence_sum(b, e, s):
    if s > 0 and b > e or (s < 0 and b < e):
        return 0
    near = e - (e - b) % s
    n = (near - b) // s + 1
    return (b + near) * n // 2
