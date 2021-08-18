def sel_number(n, d):
    count = 0

    def any_invalid(digits):
        for a, b in zip(digits, digits[1:]):
            if a >= b or b - a > d:
                return True
        return False

    for i in xrange(10, n + 1):
        if any_invalid([int(c) for c in str(i)]):
            continue
        count += 1
    return count
