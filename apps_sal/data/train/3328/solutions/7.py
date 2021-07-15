import string

def caeser(message, key=1):
    letters = string.ascii_lowercase
    mask = letters[key:] + letters[:key]
    trantab = str.maketrans(letters, mask)
    return message.translate(trantab).upper()
