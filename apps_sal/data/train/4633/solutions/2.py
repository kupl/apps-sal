def convert(number):
    return ''.join([chr(int(x)) for x in map(''.join, zip(*[iter(number)] * 2))])
