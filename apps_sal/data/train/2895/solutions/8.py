import re
aeiou = re.compile(r'([aeiou]+)([^aeiou])', re.I)

def ka_co_ka_de_ka_me(word):
    return 'ka' + aeiou.sub(r'\1ka\2', word)
