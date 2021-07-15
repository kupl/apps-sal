table = str.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '@8(D3F6#!JK1MN0PQR$7UVWXY2'
)

def to_leet_speak(text):
    return text.translate(table)

