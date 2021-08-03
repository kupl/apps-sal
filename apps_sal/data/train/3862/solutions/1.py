from string import ascii_lowercase


def mirror(code, letters=ascii_lowercase):
    return code.lower().translate(str.maketrans(letters, letters[::-1]))
