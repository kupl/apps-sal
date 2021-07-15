def is_palindrome(string):
    msg = True
    stringised = str(string)
    string_length = len(stringised)
    for x in range(string_length // 2):
        if stringised[x] != stringised[-x-1]:
            msg = False
            break
    return msg
