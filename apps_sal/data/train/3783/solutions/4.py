from itertools import chain


def frame(words, char):
    size = max(map(len, words))
    frame = [char * (size + 4)]
    middle = (f'{char} {word: <{size}} {char}' for word in words)
    return '\n'.join(chain(frame, middle, frame))
