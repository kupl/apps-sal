alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def high(x):

    strings = list(x.split())
    array = []

    for word in strings:
        value = 0
        for letter in word:
            value += alphabet.index(letter) + 1
        array.append([value, word])
    array.sort()
    return array[-1][1]
