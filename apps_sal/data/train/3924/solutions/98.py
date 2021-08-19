def reverse_words(text):
  # go for it
    textlist = text.split(' ')
    textlist = map(lambda x: x[::-1], textlist)
    return ' '.join(textlist)
