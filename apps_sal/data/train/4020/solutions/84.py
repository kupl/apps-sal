validate_hello=lambda s,d=['hello','ciao','salut','hallo','hola','ahoj','czesc']:any(x in s.lower() for x in d)
