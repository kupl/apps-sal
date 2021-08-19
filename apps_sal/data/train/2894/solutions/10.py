def triple_trouble(one, two, three):
    count = 0
    length = len(one)
    string = ''
    while count < length:
        string += one[count] + two[count] + three[count]
        count += 1
    return string
