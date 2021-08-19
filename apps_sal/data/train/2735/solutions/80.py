def jumping_number(number):
    numbers = [int(n) for n in str(number)]

    # assume input number is jumping until proven otherwise
    flag = True

    # this block will be skipped by single digit inputs
    while len(numbers) > 1:
        if abs(numbers[-1] - numbers[-2]) != 1:
            flag = False
            break
        numbers.pop(-1)

    return "Jumping!!" if flag else "Not!!"
