import regex


def remove(s):
    return regex.sub('!++(?!$)', '', s)
