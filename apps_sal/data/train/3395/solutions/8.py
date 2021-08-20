def remove_duplicate_words(s):
    return (lambda x: ' '.join((e for (i, e) in enumerate(x) if e not in x[:i])))(s.split())
