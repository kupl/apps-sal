def first_non_repeating_letter(string):
    return ([a for a in string if string.lower().count(a.lower()) == 1] or [''])[0]
    #your code here

