import re


def ka_co_ka_de_ka_me(word):
    return 'ka' + re.sub('([aeiou]+)(?=[^aeiou])', '\\1ka', word, flags=re.I)
