def jumping_number(number):
    numbers = [int(a) for a in str(number)]
    for a in range(1, len(numbers)):
        if abs(numbers[a - 1] - numbers[a]) == 1:
            continue
        else:
            return "Not!!"

    return "Jumping!!"
