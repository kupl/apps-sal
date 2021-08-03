def validate_hello(greetings):
    rez = 0
    hell = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for it in greetings.lower().split(" "):
        if "".join(i.lower() for i in it if i.isalpha()) in hell:
            rez += 1
    return True if rez > 0 else False
