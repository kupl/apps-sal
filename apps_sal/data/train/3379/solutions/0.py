def encrypter(strng):
    return ''.join( c if c==' ' else chr(122 - ((ord(c)-97)+13) % 26) for c in strng )
