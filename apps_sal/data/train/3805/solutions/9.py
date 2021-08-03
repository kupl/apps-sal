def histogram(values, bin_width):
    if len(values) == 0:
        return []
    list = [values.count(digit) for digit in range(0, max(values) + 1)]
    return [sum(list[digit:digit + bin_width]) for digit in range(0, len(list), bin_width)]
