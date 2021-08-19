from re import sub, I


def autocorrect(input):
    return sub('\\b(you+|u)\\b', 'your sister', input, flags=I)
