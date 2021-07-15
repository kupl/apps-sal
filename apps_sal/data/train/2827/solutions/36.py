ENGLISH_NUMBE_NAMES = ("Zero", "One", "Two", "Three", "Four",
                       "Five", "Six", "Seven", "Eight", "Nine")

def switch_it_up(number: int) -> str:
    """Return english names of number 0-9."""
    if 0 <= number < len(ENGLISH_NUMBE_NAMES): 
        return ENGLISH_NUMBE_NAMES[number]
    else:
        return str(number)
