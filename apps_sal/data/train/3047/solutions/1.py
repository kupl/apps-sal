def repeating_fractions(n, d):
    return __import__('re').sub('(\\d)(\\1+)(?!\\.)', '(\\1)', str(n / float(d)))
