def string_clean(s):
    new=''
    for item in s:
        if item.isnumeric():
            pass
        else:
            new+=item
    return new
