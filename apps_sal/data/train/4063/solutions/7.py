import re


def evenator(s):
    return ' '.join(word if len(word) % 2 == 0 else word + word[-1] for word in re.sub('[.,?!_]', '', s).split())
