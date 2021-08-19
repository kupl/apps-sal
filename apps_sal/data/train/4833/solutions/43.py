def replace_exclamation(s):
    import re
    return re.sub('[A|E|I|O|U|a|e|i|o|u]', '!', s)
