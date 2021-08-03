def remove(s):
    return ' '.join(i.rstrip('!') for i in s.split())
