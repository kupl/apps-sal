def loneliest(number):
    digits = []
    while number:
        (number, rem) = divmod(number, 10)
        digits.append(rem)
    lowest = one = float('inf')
    for (i, d) in enumerate(digits):
        s = sum(digits[max(0, i - d):i + d + 1]) - d
        if d == 1:
            one = min(one, s)
        else:
            lowest = min(lowest, s)
    return one <= lowest and one != float('inf')
