def compare(s1,s2):
    if type(s1) != str or not s1.isalpha(): s1 = ''
    if type(s2) != str or not s2.isalpha(): s2 = ''
    return sum(ord(i.upper()) for i in s1) == sum(ord(i.upper()) for i in s2)
