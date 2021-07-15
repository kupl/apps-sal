def validate_sequence(s):
    return sum(s) == (s[0] + s[-1]) * len(s) /2
