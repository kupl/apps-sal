from re import sub


def toUnderScore(name):
    return sub('([a-zA-Z](?=[A-Z0-9])|\\d(?=[A-Z]))', '\\1_', name)
