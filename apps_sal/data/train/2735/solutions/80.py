def jumping_number(number):
    numbers = [int(n) for n in str(number)]
    flag = True
    while len(numbers) > 1:
        if abs(numbers[-1] - numbers[-2]) != 1:
            flag = False
            break
        numbers.pop(-1)
    return 'Jumping!!' if flag else 'Not!!'
