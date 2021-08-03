def round_to_five(numbers):
    return [int(((x // 5) + (x % 5 >= 2.5)) * 5) for x in numbers]
