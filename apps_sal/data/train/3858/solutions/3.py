import re
def unscramble_eggs(word):
    return re.sub('([^aeiouAEIOU])egg', r'\1', word)
