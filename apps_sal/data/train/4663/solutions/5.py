import re


class Word(object):

    digit_regex = re.compile(r'[0-9]')

    def __init__(self, word):
        self._index = self.digit_regex.findall(word)[0]
        self._word = word

    def __repr__(self):
        return self._word

    @property
    def word(self):
        return self._word

    @property
    def index(self):
        return self._index


class Sentence(object):

    def __init__(self, words):
        self._words = words

    def __repr__(self):
        return ' '.join([str(x) for x in self.ordered()])

    def ordered(self):
        return sorted(self._words, key=lambda word: word.index)


def order(sentence):
    return str(Sentence(list(map(Word, sentence.split()))))
