def validate_hello(greetings):
    return bool([1 for x in greetings.translate(greetings.maketrans('', '', '.,!?;:')).lower().split() if x in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']])
