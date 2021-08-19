def reverse_letter(string):
    res = ''.join([a for a in string[::-1] if a.isalpha()])
    return res
