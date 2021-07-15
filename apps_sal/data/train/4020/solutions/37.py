import re


def validate_hello(greetings):
    list_hello = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    greetings2 = (re.sub("[,?!;.:]", "", greetings).lower().split())
    set_A = set(list_hello)
    set_B = set(greetings2)
    return True if set_A.intersection(set_B) != set() else False
