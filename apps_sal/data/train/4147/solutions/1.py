def play_pass(s, n):
    slower = s.lower()
    change = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for (i, char) in list(enumerate(slower)):
        if char in alphabet:
            ind = alphabet.index(char) + n
            if ind >= 26:
                ind = ind % 26
            if i % 2 == 0:
                change += alphabet[ind].upper()
            else:
                change += alphabet[ind].lower()
        elif char.isdigit():
            change += str(9 - int(char))
        else:
            change += char
    return change[::-1]
