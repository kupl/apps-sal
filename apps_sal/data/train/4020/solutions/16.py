def validate_hello(greetings):
    greetings = greetings.lower()
    return greetings.__contains__('hello') or greetings.__contains__('ciao') or greetings.__contains__('salut') or greetings.__contains__('hallo') or greetings.__contains__('hola') or greetings.__contains__('ahoj') or greetings.__contains__('czesc')
