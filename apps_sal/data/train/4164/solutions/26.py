def first_non_repeating_letter(some_string):
    # List comprehension:
    #    examine each character in the given string
    #    if the character appears only once, add it to the list
    #    otherwise, add an empty character
    #    join the list back into a string (eliminates empty characters)
    #    now the first character in our string will be the first non-repeating character
    #        NOTE: by using a one-character slice [:1] instead of an index [0] we allow
    #              it to pick up a blank character '' if the string is empty instead of
    #              giving an error for an index that is out of range.
    return ''.join([char if some_string.lower().count(char.lower()) == 1 else '' for char in some_string])[:1]
