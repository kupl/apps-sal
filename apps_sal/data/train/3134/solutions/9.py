is_valid = lambda idn: __import__("re").match(r'^[a-zA-Z_\$][a-zA-Z0-9_\$]*$', idn) is not None
