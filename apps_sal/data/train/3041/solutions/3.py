from re import sub


def vowel_start(st):
    return sub(r"\B([aeiou])", r" \1", ''.join(filter(str.isalnum, st)).lower())
