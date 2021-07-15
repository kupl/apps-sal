def longest(words):
    number_of_chars = [len(word) for word in words]
    return max(number_of_chars)
