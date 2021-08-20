def missing_alphabets(s):
    return ''.join(sorted((c * (max((s.count(x) for x in s)) - s.count(c)) for c in 'abcdefghijklmnopqrstuvwxyz')))
