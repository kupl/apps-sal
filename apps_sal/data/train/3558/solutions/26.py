def capitalize_word(word):
    ls = list(word) # Turns string into a list of characters
    ls[0] = ls[0].upper() # Makes the first letter a capital
    return "".join(ls) # Joins the list elements back into a string.
