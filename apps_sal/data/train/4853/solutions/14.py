def double_char(s):
    slowo = ""   # defining new empty string for doubled word
    for char in s:      # loop going by every char in word s
        char = 2 * char     # for every char doubling it
        slowo += char   # adding doubled char to new string
    return slowo
