def validate_hello(greetings):
    #your code here
    hello = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    greetings = greetings.lower()
    for i in hello :
        if i in greetings : return True
    else : return False
