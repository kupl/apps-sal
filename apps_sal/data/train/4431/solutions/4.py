def decode(message):
    output = ''
    for letter in message:
        if letter != ' ':
            output += chr(ord('z') - (ord(letter) - ord('a')))
        else:
            output += letter
    return output
