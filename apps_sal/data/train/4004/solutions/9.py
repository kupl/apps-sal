def first_dup(text):
    for t in text:
        if text.count(t) > 1:
            return t
