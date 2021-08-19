def reverse_words(text):
  # go for it
    string = text.split(' ')
    for i, j in enumerate(string):
        string[i] = j[::-1]
    return ' '.join(string)
