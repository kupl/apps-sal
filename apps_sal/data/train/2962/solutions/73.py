def divisible_by(numbers, divisor):
    res = []
    for i in numbers:
        if not i % divisor:
            res.append(i)
    return res
