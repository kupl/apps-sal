def to_acronym(input):
    fstring = ""
    fstring += input[0].upper()
    for i in range(0, len(input)):
        if input[i] == " ":
            fstring += input[i+1].upper()
            
    return fstring
    pass
