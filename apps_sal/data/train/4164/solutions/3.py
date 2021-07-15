def first_non_repeating_letter(string):
    
    s = string.lower()
    
    for i in string:
        if s.count(i.lower()) == 1:
            return i
    return ''
