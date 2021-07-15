def cypher(string):
    key = {
        'l':1, 'I':1, 'z':2, 'R':2, 'e':3, 'E':3, 'a':4, 'A':4, 's':5,
        'S':5, 'b':6, 'G':6, 't':7, 'T':7, 'B':8, 'g':9, 'o':0, 'O':0,
        }
    encrypt = ""
    for char in string :
        try :
            encrypt += str(key[char])
        except :
            encrypt += char
    return encrypt
