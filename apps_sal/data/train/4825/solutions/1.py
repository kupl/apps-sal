def decrypt(test_key):
    return "".join( str(test_key.count(char)) for char in "abcdefghijklmnopqrstuvwxyz" )
