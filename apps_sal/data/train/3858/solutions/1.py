from re import sub


def unscramble_eggs(word):
    return sub('([^aieou])egg', '\\1', word)
