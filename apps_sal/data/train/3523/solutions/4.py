def password(string):
    if len(string) >= 8:
        check = 0
        for c in string:
            if c.isupper():
                check |= 1
            elif c.islower():
                check |= 2
            elif c.isdigit():
                check |= 4
            if check == 7:
                return True
    return False
