VALUES = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}


def parse_int(string):
    if not string:
        return 0
    if string == 'one million':
        return 1000000
    if string in VALUES:
        return VALUES[string]
    if 'thousand' in string:
        (before, after) = split(string, 'thousand and') if 'thousand and' in string else split(string, 'thousand')
        factor = 1000
    elif 'hundred' in string:
        (before, after) = split(string, 'hundred and') if 'hundred and' in string else split(string, 'hundred')
        factor = 100
    elif '-' in string:
        (before, after) = split(string, ' ') if ' ' in string else split(string, '-')
        factor = 1
    return parse_int(before) * factor + parse_int(after)


def split(string, separator):
    (before, after) = string.rsplit(separator, 1)
    return (before.strip(), after.strip())
