import re


def ka_co_ka_de_ka_me(word):
    return 'ka' + re.sub('([aeiouAEIOU]+)([^aeiouAEIOU])', lambda x: x.group(1) + 'ka' + x.group(2), word)
