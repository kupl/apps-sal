validate_hello = lambda greetings: any(i in greetings.lower() for i in {'hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'})
