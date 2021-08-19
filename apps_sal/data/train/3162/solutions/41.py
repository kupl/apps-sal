def compare(s1, s2):
    import string
    if s1 == None or all((char in string.ascii_letters for char in s1)) == False:
        s1 = ''
    else:
        s1 = s1.upper()
    if s2 == None or all((char in string.ascii_letters for char in s2)) == False:
        s2 = ''
    else:
        s2 = s2.upper()
    lst1 = [ord(char) for char in s1]
    lst2 = [ord(char) for char in s2]
    return sum(lst1) == sum(lst2)
