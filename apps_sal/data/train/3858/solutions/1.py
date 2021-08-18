from re import sub


def unscramble_eggs(word):
    return sub(r'([^aieou])egg', r'\1', word)
