def disarium_number(number):
    sum_d = 0
    for index, d in enumerate(str(number), start=1):
        sum_d += int(d)**index
    return 'Disarium !!' if sum_d == number else 'Not !!'

