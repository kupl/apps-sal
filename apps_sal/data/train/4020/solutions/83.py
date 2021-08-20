def validate_hello(greetings: str) -> bool:
    m = greetings.casefold()
    return any((w in m for w in ('hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc')))
