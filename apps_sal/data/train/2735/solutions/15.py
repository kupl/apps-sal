def jumping_number(number):
    numbers = [int(i) for i in str(number)]
    for i in range(1, len(numbers)):
        if abs(numbers[i - 1] - numbers[i]) == 1:
            continue
        else:
            return 'Not!!'
    return 'Jumping!!'
