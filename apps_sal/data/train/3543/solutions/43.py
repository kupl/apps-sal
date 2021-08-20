import re


def increment_string(s):
    if re.match('.*?([0-9]+)$', s) == None:
        return s + '1'
    last_digits = re.match('.*?([0-9]+)$', s).group(1)
    first_letters = s.rstrip(last_digits)
    print(s)
    return first_letters + str(int(last_digits) + 1).zfill(len(last_digits))
