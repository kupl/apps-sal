def calc(x):
    total1 = ''.join((str(ord(char)) for char in x))
    total2 = total1.replace('7', '1')
    return sum((int(x) for x in total1)) - sum((int(x) for x in total2))
