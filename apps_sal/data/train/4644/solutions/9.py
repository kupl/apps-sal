def char_to_ascii(s):
    return {ch:ord(ch) for ch in set(s) if ch.isalpha()} if s else None
