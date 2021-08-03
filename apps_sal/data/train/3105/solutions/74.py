def count_sheep(n):
    phrase = ''
    for i in range(n):
        phrase += str((1 * i) + 1) + ' sheep...'
    return phrase
