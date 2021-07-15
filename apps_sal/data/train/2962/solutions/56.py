def divisible_by(numbers, divisor):
    num_list = []
    for n in numbers:
        if n % divisor == 0:
            num_list.append(n)
    return num_list

