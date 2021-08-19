def jumping_number(number):
    digits = [int(i) for i in str(number)]
    if len(digits) == 1:
        return 'Jumping!!'
    else:
        deltas = (abs(x - y) for (x, y) in zip(digits, digits[1:]))
        return 'Jumping!!' if all((delta == 1 for delta in deltas)) else 'Not!!'
