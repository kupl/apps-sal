from string import ascii_lowercase as alc


def unlock(message):
    return message.lower().translate(str.maketrans(alc, '22233344455566677778889999'))
