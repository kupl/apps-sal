def name_in_str(str, name):
    str = str.lower()
    name = name.lower()

    for n in name:
        try:
            ix = str.index(n)
            str = str[ix + 1:]
        except:
            return False
    return True
