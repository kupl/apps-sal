def capitals_first(string):
    return ' '.join([word for word in string.split() if word[0].isupper()] + [word for word in string.split() if word[0].islower()])
