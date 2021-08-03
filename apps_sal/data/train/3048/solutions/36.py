def alternateCase(s):
    string = ""
    for letter in s:
        if letter == letter.upper():
            letter = letter.lower()
            string = string + letter
        else:
            letter = letter.upper()
            string = string + letter

    return string
