def array_leaders(numbers):
    rl = []
    sarr = sum(numbers)
    for num in numbers:
        sarr -= num
        if num > sarr:
            rl.append(num)
    return rl
