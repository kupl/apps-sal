def make_upper_case(s):
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    lowers_list = [l for l in lowers]
    uppers_list = [l for l in uppers]
    dictio = dict(zip(lowers_list, uppers_list))
    output = ''
    for letter in s:
        if letter not in lowers:
            output += letter
        else:
            output += dictio[letter]
    return output
