def to_leet_speak(string):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    leet_speak = "@8(D3F6#!JK1MN0PQR$7UVWXY2"
    leet = dict(list(zip(uppercase_letters, leet_speak)))
    
    leet_builder = str()
    for letter in string:
        leet_letter = leet.get(letter)
        leet_builder += leet_letter if leet_letter else letter
    
    return leet_builder

