from string import ascii_lowercase as abc
from string import ascii_uppercase as ABC

def rot13(message):
    abc_message = abc + ABC
    abc_cipher = abc[13:] + abc[:13] + ABC[13:] + ABC[:13]
    return message.translate(str.maketrans(abc_message, abc_cipher))
