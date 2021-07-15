def unlock(message):
    return message.lower().translate(str.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        '22233344455566677778889999'))
