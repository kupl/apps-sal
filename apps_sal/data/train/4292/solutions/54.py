def string_clean(s):
    word = ""
    digits = "1234567890"
    for element in s:
        if element not in digits:
            word += element
    return word
