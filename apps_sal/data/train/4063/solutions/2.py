from re import sub


def evenator(s):
    return ' '.join((word + word[-1] if len(word) % 2 else word for word in sub('[.,?!_]', '', s).split()))
