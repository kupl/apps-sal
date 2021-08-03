def reverse_letter(line):
    letters = list(filter(str.isalpha, list(line)))
    letters.reverse()
    return ''.join(letters)
