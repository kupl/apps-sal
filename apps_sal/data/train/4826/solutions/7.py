import re


def count_robots(a):
    automatik = 0
    mechanik = 0
    for s in a:
        c = len(re.findall(r'[a - z][\|\}; &
        if 'automatik' in s.lower():
            automatik += c
        elif 'mechanik' in s.lower():
            mechanik += c
    return ["{} robots functioning automatik".format(automatik), "{} robots dancing mechanik".format(mechanik)]
