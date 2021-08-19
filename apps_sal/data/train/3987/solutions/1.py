def spin_words(sentence):
    words = [word for word in sentence.split(' ')]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return ' '.join(words)
