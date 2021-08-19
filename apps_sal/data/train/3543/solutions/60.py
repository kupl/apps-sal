import re


def increment_string(strng):
    item = strng[::-1]
    pattern = '\\d+'
    number = re.search(pattern, item)
    if number:
        reversed_word = re.split(pattern, item, 1)[1]
        reversed_num = number.group()
        num = reversed_num[::-1]
        if num == '9':
            num = '10'
        elif len(num) > 1:
            length = len(num)
            number = int(num) + 1
            number = str(number)
            num = number.zfill(length)
        else:
            num = int(num) + 1
    else:
        return strng + '1'
    return reversed_word[::-1] + str(num)
