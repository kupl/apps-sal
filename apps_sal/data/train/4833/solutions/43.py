def replace_exclamation(s):
    import re
    return re.sub(r"[A|E|I|O|U|a|e|i|o|u]", "!", s)
