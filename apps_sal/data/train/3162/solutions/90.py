def compare(s1,s2):
    if not s1 or not all(map(str.isalpha, s1)):
        s1 = ''       
    if not s2 or not all(map(str.isalpha, s2)):
        s2 = ''
    return sum(map(ord, s1.upper())) == sum(map(ord, s2.upper()))
