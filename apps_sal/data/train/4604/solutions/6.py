import re


def palindrome(num):
    if not (isinstance(num, int) and num > 0):
        return 'Not valid'
    return bool(re.search('(.)\\1|(.).\\2', str(num)))
