import re
aeiou = re.compile('([aeiou]+)([^aeiou])', re.I)


def ka_co_ka_de_ka_me(word):
    return 'ka' + aeiou.sub('\\1ka\\2', word)
