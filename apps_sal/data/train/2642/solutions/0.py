def swap_case(s):
    newstring = ""

    for item in s:
        if item.isupper():
            newstring += item.lower()
        else:
            newstring += item.upper()

    return newstring
