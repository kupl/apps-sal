def char_to_ascii(string):
    # Good Luck!
    return {x: ord(x) for x in set(string) if x.isalpha()} or None
