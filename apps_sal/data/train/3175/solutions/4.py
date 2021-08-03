import re


def triple_double(num1, num2):
    str = "{0}|{1}".format(num1, num2)
    regex = re.compile(r'(\d)(\1){2}.*\|.*(\1){2}')
    match = regex.search(str)
    return True if match else False
