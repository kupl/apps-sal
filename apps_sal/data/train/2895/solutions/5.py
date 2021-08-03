import re

r = re.compile('[aeiou]+', re.I)


def ka_co_ka_de_ka_me(word):
    word = 'ka' + r.sub(lambda m: m.group(0) + 'ka', word)
    return word[:-2] if word.endswith('ka') else word
