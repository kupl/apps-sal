table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "22233344455566677778889999")

def unlock(message):
    return message.lower().translate(table)
