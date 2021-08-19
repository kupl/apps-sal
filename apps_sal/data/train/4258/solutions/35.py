def series_sum(n):
    result = 0
    for i in range(0, n):
        result += 1.0 / (1 + 3 * i)
    stringresult = str(round(result, 2))
    if stringresult == '0':
        stringresult = '0.00'
    while len(stringresult) < 4:
        stringresult += '0'
    return stringresult
