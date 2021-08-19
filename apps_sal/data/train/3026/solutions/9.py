def min_value(digits):
    unique_digits = []
    digits.sort()
    for i in digits:
        if i not in unique_digits:
            unique_digits.append(i)
    return int(''.join((str(e) for e in unique_digits)))
