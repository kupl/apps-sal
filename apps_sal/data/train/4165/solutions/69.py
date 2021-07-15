def uni_total(string):
    letters = list(string)
    total = 0
    for letter in letters:
        total = total + ord(letter)
    return total
