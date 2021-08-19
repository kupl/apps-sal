def presses(phrase):
    numbers = ['*', '#', '1', 'ABC2', 'DEF3', 'GHI4', 'JKL5', 'MNO6', 'PQRS7', 'TUV8', 'WXYZ9', ' 0']
    print(phrase)
    phrase = phrase.upper()
    result = 0
    for letter in phrase:
        for n in numbers:
            if letter in n:
                result = result + n.index(letter) + 1
    return result
