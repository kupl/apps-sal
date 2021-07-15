def bool_to_word(boolean):
    if type(boolean) != bool:
        return 'Not a boolean!'
    else:
        return 'Yes' if boolean else 'No'
