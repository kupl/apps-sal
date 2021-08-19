from re import sub


def scratch(lottery):
    return sum((int(sub('[^\\d]', '', ch)) for ch in lottery if len(set(ch.split())) == 2))
