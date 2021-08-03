def validate_hello(greetings):
    greeting = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    t_or_f = ["True" for i in greeting if i in greetings.lower()]
    return "True" in t_or_f
