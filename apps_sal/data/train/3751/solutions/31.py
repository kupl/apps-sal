def bool_to_word(boolean):
    if bool(boolean) == 1:
        boolean = "Yes"
    if bool(boolean) == 0:
        boolean = "No"
    return boolean
