def sum_digits(number):
    string = str(number)
    for char in string:
        if char == '-':
            string = string.replace(char, '')
    return sum([int(x) for x in string])
