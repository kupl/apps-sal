def owl_pic(text):
    allowed = ('8', 'W', 'T', 'Y', 'U', 'I', 'O', 'A', 'H', 'X', 'V', 'M')
    wings = ''
    for letter in text:
        if letter.upper() in allowed:
            wings += str(letter.upper())
    return wings + "''0v0''" + wings[::-1]
