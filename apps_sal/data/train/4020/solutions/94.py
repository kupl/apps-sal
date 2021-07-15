def validate_hello(greetings):
  different_greetings = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
  return any(greeting in greetings.lower() for greeting in different_greetings)
