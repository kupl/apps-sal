def reverse_letter(string):
    # do your magic here
    newString = ""
    for word in string:
        if word.isalpha():
            newString = word + newString

    return newString
