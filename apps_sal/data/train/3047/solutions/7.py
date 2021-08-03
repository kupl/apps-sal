from re import sub
def repeating_fractions(n, d): return (lambda div: (lambda index: div[:index] + sub(r"(\d)\1+", "(\g<1>)", div[index:]))(div.index(".")))(str(1.0 * n / d))
