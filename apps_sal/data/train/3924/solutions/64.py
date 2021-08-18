def reverse_words(text):
    words = text.split(" ")
    reversed_t = " ".join(reversed(words))
    return reversed_t[::-1]
