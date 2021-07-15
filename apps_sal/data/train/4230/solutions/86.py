def reverse_letter(string):
    return ''.join((string[i] if string[i].isalpha() else "") for i in reversed(list(range(len(string)))))


