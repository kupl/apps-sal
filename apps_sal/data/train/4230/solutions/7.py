def reverse_letter(string):
    result = ''

    for char in string:
        if char.islower():
            result = char + result

    return result
