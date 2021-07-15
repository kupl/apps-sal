def longer(s):
    return ' '.join(sorted(sorted(s.split(' ')), key=len))
