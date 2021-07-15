import re

def kontti(s):
    return  " ".join( [ re.sub("([^aeiouy]*[aeiouy])(.*)", r"ko\2-\1ntti", w, flags = re.I) for w in s.split() ] )
