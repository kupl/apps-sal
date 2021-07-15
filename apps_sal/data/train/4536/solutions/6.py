def capitals_first(text):
    # one-line
    #return " ".join(sorted((word for word in text.split(" ") if word[0].isalpha()), key=lambda word: word[0].islower()))
    upper, lower = [], []
    for word in text.split(" "):
        if word[0].islower():
            lower.append(word)
        elif word[0].isupper():
            upper.append(word)
    return " ".join(upper + lower)
