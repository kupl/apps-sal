import re

def replace_exclamation(s: str) -> str:
    """ Replace all vowel to exclamation mark in the sentence. `aeiouAEIOU` is vowel. """
    return re.sub("[AEIOUaeiou]", "!", s)
