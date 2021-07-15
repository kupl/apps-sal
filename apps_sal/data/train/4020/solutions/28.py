import re
def validate_hello(greetings):
    greetings = greetings.lower()
    a = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for i in a:
        x = re.findall(str(i), greetings)
        if not x:
            pass
        else:
            return True
    return False
