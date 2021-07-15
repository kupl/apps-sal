from re import sub
def unscramble_eggs(word):
    # Geggoodegg Legguceggkegg!
    return sub(r'([^aieou])egg',r'\1', word)
