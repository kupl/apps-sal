def capitals_first(text):
    words = text.split()
    lower, upper = [], []
    for w in words:
        if w[0].islower():
            lower.append(w)
        elif w[0].isupper():
            upper.append(w)
    return " ".join(upper + lower)
