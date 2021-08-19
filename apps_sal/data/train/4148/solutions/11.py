def sum_digits(number):
    sum = 0
    if len(str(number)) == 1:
        return number
    else:
        for i in range(len(str(number))):
            if str(number)[i] == '-':
                sum += 0
            else:
                sum += int(str(number)[i])
        return sum
