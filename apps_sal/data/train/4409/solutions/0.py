def noonerize(numbers):
    try:
        num1 = int(str(numbers[1])[0] + str(numbers[0])[1:])
        num2 = int(str(numbers[0])[0] + str(numbers[1])[1:])
    except ValueError:
        return 'invalid array'
    return abs(num1 - num2)
