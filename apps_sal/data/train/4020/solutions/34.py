def validate_hello(greetings):
    greets = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    text_words = greetings.lower()
    
    return any(i in text_words for i in greets)
