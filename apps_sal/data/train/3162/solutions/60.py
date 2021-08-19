def ascii(x):
    return ord(x.upper())


def compare(s1, s2):
    if s1 == None:
        s1 = ''
    if s2 == None:
        s2 = ''
    if not s1.isalpha():
        s1 = ''
    if not s2.isalpha():
        s2 = ''
    return sum((ascii(i) for i in s1)) == sum((ascii(i) for i in s2))
