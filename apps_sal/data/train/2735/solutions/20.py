def jumping_number(number):
    numbers = [int(x) for x in str(number)]
    diff = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    if diff.count(1) + diff.count(-1) == len(numbers) - 1 or len(diff) == 0:
        return 'Jumping!!'
    else:
        return 'Not!!'
