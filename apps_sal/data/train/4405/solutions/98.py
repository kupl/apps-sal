def is_palindrome(string):
    subString = str(string)
    control = True
    for i in range(0, int(len(subString) / 2)):
        if subString[i:i + 1] != subString[len(subString) - i - 1:len(subString) - i]:
            control = False
            break
    return control
