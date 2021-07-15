def mirror(message, key="abcdefghijklmnopqrstuvwxyz"):
    return message.lower().translate(str.maketrans(key, key[::-1]))
