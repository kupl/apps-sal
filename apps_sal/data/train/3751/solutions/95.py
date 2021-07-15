def bool_to_word(boolean):
    if type(boolean) == type(True):
        if boolean:
            return 'Yes'
        else:
            return 'No'
    else:
        raise TypeError("boolean was not of type boolean but of type {}".format(type(boolean)))
