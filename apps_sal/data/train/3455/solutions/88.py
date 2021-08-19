def disarium_number(number):
    e = 0
    s = 0
    for x in str(number):
        e += 1
        s += int(x) ** e
    return 'Disarium !!' if s == number else 'Not !!'
