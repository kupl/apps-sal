def spin_words(sentence):
    output = []
    for word in sentence.split(' '):
        if len(word) > 4:
            word = word[::-1]
        output.append(word)
    return ' '.join(output)
