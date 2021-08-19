def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    res = []
    for number in range(a, b + 1):
        digits = [int(i) for i in str(number)]
        s = 0
        for idx, val in enumerate(digits):
            s += val ** (idx + 1)
        if s == number:
            res.append(number)
    return res
