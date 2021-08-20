import re


def autocorrect(i):
    return ' '.join((re.sub('^(y+o+u+|u)([,.!])?$', 'your sister\\2', word, flags=re.IGNORECASE) for word in i.split()))
