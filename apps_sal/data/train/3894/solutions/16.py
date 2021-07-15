def solve(s):
    count_u = 0
    count_l = 0
    for letter in s:
        if letter.isupper():
            count_u += 1
        elif letter.islower():
            count_l += 1
    if count_u > count_l:
        return s.upper()
    else:
        return s.lower()
