def validate_hello(greetings):
    lista = ['hello','ciao','salut','hallo','hola','ahoj','czesc']
    for i in lista:
        if i.lower() in greetings.lower():
            return True
            
    return False
