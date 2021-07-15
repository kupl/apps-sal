def min_value(digits):
    digits = sorted(list(dict.fromkeys(digits))) #removes duplicates and sorts the list
    digits = ''.join(list(map(str,digits))) #converts the list into a string
    return int(digits) #converts the string into an integer

