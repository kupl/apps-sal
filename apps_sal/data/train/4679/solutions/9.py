def to_freud(sentence):
    sentence = sentence.split()
    sentence = ['sex' for i in range(len(sentence))]
    sentence = ' '.join(sentence)
    return sentence
