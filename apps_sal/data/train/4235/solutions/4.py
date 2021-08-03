def make_sentences(parts):
    return ' '.join(x for x in parts if x != '.').replace(' ,', ',') + '.'
