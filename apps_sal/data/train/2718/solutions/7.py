def timed_reading(max_length, text):
    return sum([1 for w in text.split() if 0 < len(''.join(filter(str.isalpha, w))) <= max_length])
