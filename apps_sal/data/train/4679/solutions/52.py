def to_freud(sentence):
    return '' if sentence == '' else 'sex ' * (len(sentence.split()) - 1) + 'sex'
