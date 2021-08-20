import re


def replace_exclamation(string):
    return re.sub('[aeiouAEIOU]', '!', string)
