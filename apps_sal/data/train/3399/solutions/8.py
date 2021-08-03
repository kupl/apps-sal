from string import ascii_lowercase

pos = {x: i for i, x in enumerate(ascii_lowercase)}


def alpha_seq(string):
    return ','.join(x.upper() + x.lower() * pos[x] for x in sorted(string.lower()))
