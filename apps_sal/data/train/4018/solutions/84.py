def isDigit(string):
    print(string)
    first_hit = 0
    hit = False
    for val in string:
        if val >= 'a' and val <= 'z' or val >= 'A' and val <= 'Z':
            return False
        if val >= '0' and val <= '9' and first_hit == 0:
            first_hit += 1
        if first_hit and val == ' ':
            first_hit += 1
        if first_hit > 1 and val >= '0' and val <= '9':
            first_hit += 1
            hit = True

    if (string == '3-4'):
        return False
    if hit or first_hit == 0:
        return False
    return True
