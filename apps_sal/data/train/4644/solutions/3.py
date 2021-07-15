char_to_ascii = lambda s: {e:ord(e) for e in set(s) if e.isalpha()} or None

