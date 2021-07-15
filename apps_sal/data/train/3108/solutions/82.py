def multi_table(number):
    a = []
    for i in range(1, 11):
        a.append(i * number)
    b = ""
    count = 1
    for i in a:
        b += str(count) + " * " + str(number) + " = " + str(i) + "\n"
        count += 1
    return b[0:-1]
