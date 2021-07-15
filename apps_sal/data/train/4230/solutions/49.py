def reverse_letter(string):
    reversed = ''
    for char in string:
        if char.isalpha():
            reversed += char
    return reversed[::-1]


