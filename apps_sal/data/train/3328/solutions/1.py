def caeser(message, key):
    return ''.join((chr(ord(x) + key if ord(x) + key <= 122 else ord(x) + key - 122 + 96).upper() if x.isalpha() else x for x in message))
