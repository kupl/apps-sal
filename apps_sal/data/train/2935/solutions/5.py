import re

def is_vowel(s):
    return True if re.match(r"^[AaEeIiOoUu](?!\n)$", s) else False
