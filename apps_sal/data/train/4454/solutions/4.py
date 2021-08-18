def presses(phrase):
    numbers = ['*', '
    print(phrase)
    phrase = phrase.upper()
    result = 0

    for letter in phrase:
        for n in numbers:
            if letter in n:
                result = result + n.index(letter) + 1
    return result
