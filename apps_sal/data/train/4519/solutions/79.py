def max_number(n):
    numbers = []
    for number in str(n):
        numbers.append(number)
    numbers = sorted(numbers, reverse=True)
    numbers = ''.join(map(str, numbers))
    return int(numbers)
