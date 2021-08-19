def find_all(sum_dig, digs):
    if sum_dig > 9 * digs:
        return []
    all = [x for x in growing_digits(digs - 1) if digit_sum(x) == sum_dig]
    return [len(all), all[0], all[-1]]


def digit_sum(num):
    """ returns the sum of the digits of a number """
    return sum((int(digit) for digit in str(num)))


def growing_digits(order, start=1):
    """ A little recursive generator magic
        returns all numbers of order+1 digits
        such that the digits are non-decreasing
    """
    for l in range(start, 10):
        if order == 0:
            yield l
        else:
            for r in growing_digits(order - 1, start=l):
                yield (l * 10 ** order + r)
