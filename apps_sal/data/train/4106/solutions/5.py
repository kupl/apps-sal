def self_converge(number):
    digits = len(str(number))
    if digits < 3 or number % int('1' * digits) == 0:
        return -1
    fmtstr = '%%0%dd' % digits
    log = [number]
    while True:
        nstr = fmtstr % number
        low = int(''.join(sorted(nstr)))
        high = int(''.join(sorted(nstr, reverse=True)))
        nextn = high - low
        if nextn in log:
            return len(log)
        log.append(nextn)
        number = nextn
