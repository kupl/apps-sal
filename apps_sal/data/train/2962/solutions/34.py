def divisible_by(numbers, divisor):
    new_list = []
    for elem in numbers:
        if elem % divisor == 0:
            new_list.append(elem)
    return new_list
