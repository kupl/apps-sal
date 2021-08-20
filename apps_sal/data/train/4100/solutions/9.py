def reverse_alternate(string):
    return ' '.join([word[::-1] if string.split().index(word) % 2 != 0 else word for word in string.split()])
