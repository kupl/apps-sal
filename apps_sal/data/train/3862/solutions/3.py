def mirror(code, opt=None):
    if opt == None:
        key = "abcdefghijklmnopqrstuvwxyz"
    else:
        key = opt

    result = ''
    for letter in code.lower():
        try:
            result += key[-1 - key.index(letter)]
        except:
            result += letter

    return result
