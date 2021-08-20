def toDex(n):
    return int(n[-1]) - 2 * toDex(n[:-1]) if n else 0


def toBin(n):
    return toBin((n - n % 2) / -2) + str(n % 2) if n else ''


def skrzat(base, number):
    if not number:
        return 'From decimal: 0 is 0'
    elif base in 'b':
        return 'From binary: %s is %d' % (number, toDex(number))
    elif base in 'd':
        return 'From decimal: %d is %s' % (number, toBin(number))
