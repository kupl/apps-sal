import re


def palindrome(num):
    return re.search('(\\d)\\d?\\1', str(num)) is not None if isinstance(num, int) and num > 0 else 'Not valid'
