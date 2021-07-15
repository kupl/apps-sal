#from string import ascii_lowercase as LOWER
LOWER = "abcdefghijklmnopqrstuvwxyz"

def encode(message, key, shift, encode=True):
    key = sorted(LOWER, key=f"{key}{LOWER}".index)
    result = []
    for char in message:
        if char in key:
            i = key.index(char)
            char = key[(i + shift) % 26]
            shift = i + 1 if encode else -(key.index(char) + 1)
        result.append(char)
    return "".join(result)
    
def decode(message, key, shift): 
    return encode(message, key, -shift, encode=False)
