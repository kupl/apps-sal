def pig_latin(s):
    return '{}{}ay'.format(s[1:], s[0]) if len(s) > 3 else s
