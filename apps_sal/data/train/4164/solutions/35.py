def first_non_repeating_letter(string):  
    if len(string)==1 or len(string)==0:
        return string  
    for leter in string:
        if (leter.lower() not in string[string.index(leter)+1:].lower()) and (leter.lower() not in string[:string.index(leter)].lower()):
            return(leter)
    else:
        return('')
