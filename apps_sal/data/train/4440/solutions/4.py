def validate_pin(pin):
    """
    Returns True if pin is a string of 4 or 6 digits, False otherwise.
    """
    
    # First check that pin is a string of length 4 or 6
    if(type(pin) != str or len(pin) not in [4, 6]):
        return(False)

    # If any character is not a digit, return False
    for c in pin:
        if c not in "0123456789":
            return(False)

    # If all the characters are digits, return True
    return(True)

