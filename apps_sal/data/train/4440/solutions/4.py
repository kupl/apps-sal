def validate_pin(pin):
    """
    Returns True if pin is a string of 4 or 6 digits, False otherwise.
    """

    if(type(pin) != str or len(pin) not in [4, 6]):
        return(False)

    for c in pin:
        if c not in "0123456789":
            return(False)

    return(True)
