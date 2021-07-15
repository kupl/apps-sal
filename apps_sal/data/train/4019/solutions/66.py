def max_multiple(divisor, bound):
    multiple = 0
    while multiple <= bound:
        multiple += divisor
        print(multiple)
    return multiple-divisor
