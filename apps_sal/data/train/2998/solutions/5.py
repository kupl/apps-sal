def atomic_number(electrons):
    res = []
    i = 1
    while True:
        m = 2 * i ** 2
        if electrons > m:
            res.append(m)
            electrons -= m
            i += 1
        else:
            res.append(electrons)
            break
    return res
