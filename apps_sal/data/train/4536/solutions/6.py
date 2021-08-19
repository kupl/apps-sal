def capitals_first(text):
    (upper, lower) = ([], [])
    for word in text.split(' '):
        if word[0].islower():
            lower.append(word)
        elif word[0].isupper():
            upper.append(word)
    return ' '.join(upper + lower)
