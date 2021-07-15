def compare(s1,s2):

    if s1 == None or s1.isalpha() == False:
        s1 = ""
    if s2 == None or s2.isalpha() == False:
        s2 = ""

    lst1 = [ord(char) for char in s1.upper()]
    lst2 = [ord(char) for char in s2.upper()]

    return sum(lst1) == sum(lst2)
