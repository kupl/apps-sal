import re

BAD_WORD = re.compile(r'bad|mean|ugly|horrible|hideous', re.I)

GOOD_WORD = 'awesome'


def filter_words(phrase):
    return BAD_WORD.sub(GOOD_WORD, phrase)

