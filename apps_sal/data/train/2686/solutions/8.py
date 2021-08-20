def changer(string):
    string = ''.join((chr(ord(letter) + 1).upper() if chr(ord(letter) + 1) in 'aeiouAEIOU' else letter if letter in ' 0123456789' else 'A' if letter.lower() == 'z' else chr(ord(letter) + 1).lower() for letter in string))
    return string
