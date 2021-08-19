def disarium_number(number):
    a = 1
    s = 0
    for i in str(number):
        s += int(i) ** a
        a += 1
    return 'Disarium !!' if s == number else 'Not !!'
