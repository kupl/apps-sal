from re import split


def word_count(s):
    return len([w for w in split('[^a-z]+', s.lower()) if not w in ['a', 'the', 'on', 'at', 'of', 'upon', 'in', 'as', '']])
