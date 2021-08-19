def revamp(s):
    return ' '.join([x for x in sorted((''.join(sorted(x)) for x in s.split()), key=lambda x: (sum(map(ord, x)), x))])
