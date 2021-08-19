import re


def increment_string(input):
    match = re.search('(\\d*)$', input)
    if match:
        number = match.group(0)
        if number is not '':
            return input[:-len(number)] + str(int(number) + 1).zfill(len(number))
    return input + '1'
