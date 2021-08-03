from re import sub


def lowercase_count(strng):
    return len(sub('[^a-z]', '', strng))
