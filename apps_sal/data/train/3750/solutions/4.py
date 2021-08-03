import re


def count_letters_and_digits(s):
    try:
        list = re.findall('[A-Za-z0-9]', s)
        return (len(list))
    except:
        return 0
