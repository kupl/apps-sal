import re


def pig_latin(s):
    s = s.lower()
    if re.findall('[\\d\\W]', s) or s == '':
        return None
    elif s.startswith(('a', 'e', 'i', 'o', 'u')):
        return s + 'way'
    else:
        return re.sub('(^[^aeiou]+)(\\w*)', '\\g<2>\\g<1>ay', s)
