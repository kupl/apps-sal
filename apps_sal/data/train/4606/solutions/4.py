import re


def valid_romans(arr):
    pattern = re.compile('^M{0,4}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})$')
    return [number for number in arr if number and pattern.match(number)]
