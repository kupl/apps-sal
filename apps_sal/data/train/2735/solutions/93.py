def jumping_number(number):
    numbers = [int(n) for n in str(number)]
    i = 0
    while i < len(numbers) - 1:
        minus = numbers[i] - numbers[i + 1]
        plus = numbers[i + 1] - numbers[i]
        if minus != 1 and plus != 1:
            return 'Not!!'
        i += 1
    return 'Jumping!!'
