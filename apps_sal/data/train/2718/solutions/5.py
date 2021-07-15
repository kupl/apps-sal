import string

def timed_reading(max_length, text):
    return len(list([x for x in text.split() if 1 <= len(x.strip(string.punctuation)) <= max_length]))
