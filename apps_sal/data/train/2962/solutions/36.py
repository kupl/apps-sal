def divisible_by(numbers, divisor):
    final_list = []
    for num in numbers:
        if num % divisor == 0:
            final_list.append(num)
        else:
            continue
    return final_list
