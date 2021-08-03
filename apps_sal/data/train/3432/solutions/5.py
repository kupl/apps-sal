def cipher(phrase: str):
    t = [0, 2, 3]
    string = ''
    x = -1
    for i in phrase:
        x += 1
        if(ord(i) != ord(' ')):
            c = ord(i) - 97
            if(x == 0):
                string += chr(c + 97)
            elif(x == 1):
                string += chr(((c + 1) % 26) + 97)
            elif(x == 2):
                string += chr(((c + 2) % 26) + 97)
            else:
                string += chr(((c + t[x % 3] + (int)(x / 3) - 1) % 26) + 97)
        else:
            string += ' '

    print(string)
    return string
