import re
def ka_co_ka_de_ka_me(word):
    return "ka"+re.sub(r'([aeiouAEIOU]+)([^aeiouAEIOU])',lambda x: x.group(1)+r"ka"+ x.group(2),word)
