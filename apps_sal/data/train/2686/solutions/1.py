def changer(s):
    return ''.join([a if not a.isalpha() else chr((ord(a) - 96) % 26 + 97).upper() if a in 'zdhnt' else chr(ord(a) + 1) for a in s.lower()])
