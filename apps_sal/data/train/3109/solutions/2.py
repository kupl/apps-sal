import re


def scramble_words(words):
    new_words = []
    for word in words.split():
        (begin, word) = re.match("([-',.]*[a-zA-Z]?)(.*)", word).groups()
        (word, end) = re.match("(.*?)([a-zA-Z]?[-',.]*)$", word).groups() if word else ('', '')
        sorted_word = list(sorted((c for c in word if c.isalpha())))
        for (i, c) in enumerate(word):
            if c in "-',.":
                sorted_word.insert(i, c)
        new_words.append(begin + ''.join(sorted_word) + end)
    return ' '.join(new_words)
