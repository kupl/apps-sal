def replace_exclamation(s):
    new_string=""
    x = "a","e","i","o","u","A","E","I","O","U"
    for i in s:
        if i in x:
            new_string+="!"
        else:
            new_string+= str(i)
    return new_string
