def uni_total(string):
    account = 0
    for letters in string:
        if 96 < ord(letters) < 123: 
            account += ord(letters)
        else:
            64 < ord(letters) < 91
            account += ord(letters)
    return account 

