def first_non_repeating_letter(string):
    strLower = string.lower()
    for let in string:
        if strLower.count(let.lower())==1:
            return let
    return ""
            

