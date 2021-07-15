MORSE_DICT = {"-----":"0", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9"}
def morse_converter(string):
    return int( ''.join( MORSE_DICT[string[n:n+5]] for n in range(0,len(string),5) ) )
