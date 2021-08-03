def move_ten(st):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    output = ""
    for letter in st:
        index = alphabet.index(letter)
        letter = alphabet[index + 10]
        output += letter
    return output
