from re import findall

def word_count(s):
    forbidden = ['a', 'on', 'the', 'at', 'of', 'upon', 'in', 'as']
    words = ' '.join(findall(r'[a-z]+', s.lower()))
    return len([w for w in words.split() if w not in forbidden])
