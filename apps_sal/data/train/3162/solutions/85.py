def compare(s1,s2):
    if s1== None or not s1.isalpha(): s1=""
    if s2== None or not s2.isalpha(): s2=""
    return sum(ord(x.upper()) for x in s1) == sum(ord(x.upper()) for x in s2)
