def name_in_str(strng, name):
    strng = strng.lower()
    for letter in name.lower():
        if letter not in strng:
            return False
        else:
            strng = strng[strng.find(letter) + 1:]
    return True
