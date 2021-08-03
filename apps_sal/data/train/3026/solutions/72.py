def min_value(digits):
    noDuplicates = list(set(digits))
    sortedDigits = sorted(noDuplicates)

    return int(''.join([str(x) for x in sortedDigits]))
