def frogify(s):
    for c in '.!?':
        if c in s:
            return f'{c} '.join(map(frogify, s.split(c))).strip()
    words = ''.join(c for c in s.lower() if c == ' ' or 'a' <= c <= 'z').split()
    return ' '.join(words[::-1])
