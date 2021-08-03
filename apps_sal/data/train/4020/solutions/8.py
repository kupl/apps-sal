def validate_hello(g): return any(bool(g.lower().count(s)) for s in ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"])
