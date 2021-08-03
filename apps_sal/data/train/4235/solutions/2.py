import re


def make_sentences(parts):
    return re.match(r'[^\.]+', ' '.join(parts).replace(' , ', ', ')).group().strip() + '.'
