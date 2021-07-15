def uni_total(string):
    summ = 0
    for i in string:
        summ += ord(i)
    return summ if string else 0
