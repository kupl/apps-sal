def reverse_letter(string):
    word = [x for x in string[::-1] if x.isalpha()]
    return ''.join(word)
