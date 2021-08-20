def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda x: int(''.join(filter(str.isdigit, x)))))
