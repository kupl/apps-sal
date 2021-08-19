def reverse_letter(string):
    newString = ''
    for word in string:
        if word.isalpha():
            newString = word + newString
    return newString
