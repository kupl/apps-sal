def char_freq(message):
    return dict(map(lambda letter: (letter, message.count(letter)), message))
