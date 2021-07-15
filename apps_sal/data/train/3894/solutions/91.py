def solve(s):
    import string
    lower_alphabet = list(string.ascii_lowercase)
    upper_alphabet = list(string.ascii_uppercase)
    count_lower = 0
    count_upper = 0
    for i in s:
        if i in lower_alphabet:
            count_lower = count_lower + 1
        elif i in upper_alphabet:
            count_upper = count_upper + 1   
    if count_lower >= count_upper:
        s = s.lower()
    else:
        s = s.upper()
    return(s)
