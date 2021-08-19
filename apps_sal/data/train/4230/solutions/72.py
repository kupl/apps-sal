def reverse_letter(string):
    only_char = ''
    for char in string:
        if char.isalpha():
            only_char += char
    return only_char[::-1]
