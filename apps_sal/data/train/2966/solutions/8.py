def calculate(string):
    numbers = [int(x) for x in string.split() if x.isdigit()]
    return numbers[0] + numbers[1] if 'gains' in string else numbers[0] - numbers[1]
