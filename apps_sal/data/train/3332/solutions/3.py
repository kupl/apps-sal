import re


def autocorrect(input):
    return re.sub("\\b(yo[u]+|[u])(?!'\\w)\\b", 'your sister', input, flags=re.IGNORECASE)
