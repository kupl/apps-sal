def is_isogram(string):
    return len(set(list(string.lower()))) == len(string)
