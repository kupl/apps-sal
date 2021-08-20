import re


def make_sentences(parts):
    return re.match('[^\\.]+', ' '.join(parts).replace(' , ', ', ')).group().strip() + '.'
