def lucas_lehmer(n):
    m = (1 << n) - 1
    s = 4
    for i in range(n - 2):
        s = s * s - 2
        while int.bit_length(s) > n:
            s = (s >> n) + (s & m)
    return s == m or n == 2
