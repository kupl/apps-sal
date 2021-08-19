from re import sub


def vowel_start(st):
    return sub('\\B([aeiou])', ' \\1', ''.join(filter(str.isalnum, st)).lower())
