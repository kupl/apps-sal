def reverse_letter(string):
    chars_only = ''
    for item in string:
        if item.isalpha():
            chars_only += item
    return chars_only[::-1]
