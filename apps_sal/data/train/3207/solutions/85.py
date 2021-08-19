def reverseWords(str):
    words = str.split()
    words = list(reversed(words))
    reverse_str = ' '.join(words)
    return reverse_str
