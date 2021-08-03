from re import sub


def timed_reading(max_length, text):
    return sum(len(word) <= max_length for word in sub("[^a-zA-Z ]*", "", text).split())
