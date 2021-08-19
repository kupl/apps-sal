import re
KA_PATTERN = re.compile('(?![aeiou]+$)([aeiou]+)', re.I)


def ka_co_ka_de_ka_me(word):
    return 'ka' + KA_PATTERN.sub('\\1ka', word)
