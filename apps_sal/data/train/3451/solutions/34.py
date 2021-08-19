def triangle(row):
    sigue = len(row)
    renant = row
    sigren = ''
    if not 1 <= sigue <= 10 ** 5:
        return 'B'
    while sigue > 1:
        for r in range(0, len(renant) - 1, 1):
            cad = renant[r:r + 2]
            sigren += list({'R', 'G', 'B'} - set(cad) if cad[0] != cad[1] else cad[0])[0]
        renant = sigren
        sigren = ''
        sigue = len(renant)
    return renant
