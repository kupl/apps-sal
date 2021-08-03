def divisible_by(numbers, divisor):
    divisible_nums = []
    for i in numbers:
        if i % divisor == 0:
            divisible_nums.append(i)

    return divisible_nums
