def longer(sentence):

    def conditional(word):
        return (len(word), word)
    words = sentence.split(' ')
    words = sorted(words, key=conditional)
    return ' '.join(words)
