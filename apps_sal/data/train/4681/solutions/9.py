def alphabetized(s):
    return ''.join(sorted([i for i in s if i.isalpha()], key=lambda s: s.upper()))
