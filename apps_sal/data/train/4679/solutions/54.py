def to_freud(sentence):
    return (len(sentence.split()) * 'sex ' if sentence else '')[:-1]
