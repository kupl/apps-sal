import string

alpha = {x: i for i, x in enumerate(string.ascii_lowercase)}


def to_lover_case(s):
    return ''.join(
        ('LOVE'[alpha[c] % 4] if c.islower() else c)
        for c in s.lower()
    )
