from re import sub


def repeating_fractions(n, d):
    return sub('(\\d)\\1+(?!\\d*\\.)', lambda m: f'({m[1]})', str(n / d))
