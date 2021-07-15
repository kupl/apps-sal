def alphabetized(s):
    return ''.join(sorted([c for c in s if c.isalnum()], key=str.lower))
