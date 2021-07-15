def alphabetized(s):
    return ''.join(sorted( ''.join([x for x in s if x.isalpha()]) , key=lambda x: x.lower()))
