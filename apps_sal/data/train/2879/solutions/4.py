import unicodedata

def could_be(original, another):
    original, another = [set(process(s).split()) for s in (original, another)]
    return bool(another) and another <= original

def process(s):
    if isinstance(s, bytes):
        s = s.decode('utf-8')
    punct = '.!,;:?'
    s = s.translate(str.maketrans(punct, ' ' * len(punct)))
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore')
    return s.lower()
