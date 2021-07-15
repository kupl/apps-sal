def first_non_repeating_letter(string):
    for x in string:
        if x.lower() not in string.lower()[string.index(x)+1:]: return x
    else: return '' 
