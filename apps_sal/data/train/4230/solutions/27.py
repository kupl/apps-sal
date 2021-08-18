def reverse_letter(string):
    string = str().join(list(filter(str.isalpha, string)))
    return string[::-1]
