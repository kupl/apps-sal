def uni_total(string):
    account = 0
    for letters in string:
        account += ord(letters)
    return account
