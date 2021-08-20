def char_to_ascii(s):
    return {e: ord(e) for e in set(s) if e.isalpha()} or None
