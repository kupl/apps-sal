def infected(s):
    total = infected = 0
    curr = isInfected = 0
    for c in s:
        if c == '0' or c == '1':
            if c == '1':
                isInfected = -1
            curr += 1
        elif c == 'X':
            infected += curr & isInfected
            total += curr
            isInfected = curr = 0
    infected += curr & isInfected
    total += curr
    return infected / (total / 100) if total else 0
