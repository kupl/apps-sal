import re


def string_parse(string):
    if type(string) != str:
        return 'Please enter a valid string'
    for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        string = re.sub(c + '{2}(' + c + '+)', c * 2 + '[\g<1>]', string)
    return string
