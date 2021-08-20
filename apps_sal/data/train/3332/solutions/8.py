import re


def autocorrect(input):
    return re.sub('(\\bu\\b|\\byo[u]+\\b)', 'your sister', input, flags=re.IGNORECASE)
