def order(sentence):
    def sort_key(s):
        return next(c for c in s if c.isdigit())
    return ' '.join(sorted(sentence.split(), key=sort_key))
