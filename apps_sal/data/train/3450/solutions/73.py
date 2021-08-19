def array(s):
    s = s.replace(',', ' ')
    s = s.split()
    if len(s) < 3:
        return None
    return ' '.join(s[1:-1])
