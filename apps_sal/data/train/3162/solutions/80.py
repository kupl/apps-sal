def compare(s1, s2):
    integer_one = 0
    integer_two = 0
    if s1 != None:
        for i in s1.upper():
            if i.isalpha():
                integer_one = integer_one + ord(i)
            else:
                integer_one = 0
                break
    else:
        integer_one = 0
    if s2 != None:
        for ii in s2.upper():
            if ii.isalpha():
                integer_two = integer_two + ord(ii)
            else:
                integer_two = 0
                break
    else:
        integer_two = 0
    if integer_one == integer_two:
        return True
    else:
        return False
