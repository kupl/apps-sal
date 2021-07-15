TABLE = str.maketrans('iIoOsS','110055')

def make_password(s):
    return ''.join(w[0] for w in s.split()).translate(TABLE)
