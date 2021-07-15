def double_char(s):
    y = list(s) # Breaks the string into individual letters
    length = len(y) # Length of string
    ffs = list(range(0,length)) # Creates an array beginning with 0, going up in ones, the length of the original string
    blank="" # Blank string to build from
    for i in ffs: # For (i)tems in ffs, number 0 thru x (length)
        blank = blank + y[i] + y[i] # Essentially blank + list(0) + list(0), then blank + list(1) + list(1)
    return blank
