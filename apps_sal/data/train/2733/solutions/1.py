def last(s):
    return sorted(s.split(), key=lambda word: word[-1])
