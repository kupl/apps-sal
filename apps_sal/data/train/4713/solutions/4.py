def late_clock(digits):
    result = ''
    minute = '_'
    lessSix = 0
    digits = sorted(digits, reverse=True)
    for d in digits:
        if d < 6:
            lessSix += 1
    for d in digits:
        if d < 3:
            if lessSix < 3 and d == 2:
                continue
            result += str(d)
            digits.remove(d)
            break
    for d in digits:
        if (d < 4 and result == '2') or (d < 10 and result != '2'):
            result += str(d) + ':'
            digits.remove(d)
            break
    for d in digits:
        if d < 6:
            minute = str(d)
            digits.remove(d)
            break
    result += minute + str(digits.pop())
    return result
