def reverse_words(text):
    # Split ' ' will respect multiple whitespace where split() will not.
    return ' '.join(word[::-1] for word in text.split(' '))
