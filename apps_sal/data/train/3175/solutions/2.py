def triple_double(num1, num2):
    (num1, num2) = (str(num1), str(num2))
    for num in '0123456789':
        if num * 3 in num1 and num * 2 in num2:
            return 1
    return 0
