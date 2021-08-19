import re


def get_age(age):
    r = re.compile('^(\\d+) years old$')
    m = r.match(age)
    if m:
        return int(m.group(1))
    else:
        return 1
