import re


def decode(number):
    arr = []
    for match in re.finditer(r'((?:1[01][1-9]|110|12[0-7])+)98([01]+)(?:98)?', str(number)):
        arr.append(re.sub(r'\d{3}', lambda m: chr(int(m.group()) - 4), match.group(1)))
        arr.append(str(int(match.group(2), 2)))
    return ', '.join(arr)
