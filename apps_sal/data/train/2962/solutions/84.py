def divisible_by(numbers, divisor):
    n_num = []
    for i in numbers:
        if i % divisor == 0:
            n_num.append(i)
    return n_num
