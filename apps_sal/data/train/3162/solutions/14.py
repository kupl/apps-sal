def compare(s1,s2):
    if not s1 or not s1.isalpha():s1=''
    if not s2 or not s2.isalpha():s2=''
    return sum(map(ord,s1.upper())) == sum(map(ord,s2.upper()))
