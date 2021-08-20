def pig_latin(word):
    return '{}{}ay'.format(word[1:], word[0]) if len(word) > 3 else word
