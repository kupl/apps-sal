import re

KA_PATTERN = re.compile(r'(?![aeiou]+$)([aeiou]+)', re.I)


def ka_co_ka_de_ka_me(word):
    return 'ka' + KA_PATTERN.sub(r'\1ka', word)
