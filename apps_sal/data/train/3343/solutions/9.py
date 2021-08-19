def memorysize_conversion(s):
    (a, b) = s.split()
    (n, m, i) = (1024, 1000, '') if 'i' in b else (1000, 1024, 'i')
    p = ' KMGT'.index(b[0].upper())
    return f"{round(float(a) * n ** p / m ** p, 3)} {('k' if b[0] == 'K' else b[0].upper())}{i}B"
