def compare(s1, s2):
    if s1 is None:
        s1 = ''
    if s2 is None:
        s2 = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s1 = [ord(i) if i in alphabet else 0 for i in s1.upper()]
    s2 = [ord(i) if i in alphabet else 0 for i in s2.upper()]
    if 0 in s1:
        s1 = ''
    if 0 in s2:
        s2 = ''
    return sum(s1) == sum(s2)
