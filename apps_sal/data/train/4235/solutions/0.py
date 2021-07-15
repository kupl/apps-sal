def make_sentences(parts):
    return ' '.join(parts).replace(' ,', ',').strip(' .') + '.'
