def compare(s1, s2):
    try:
        comp1 = s1.upper()
        comp2 = s2.upper()
    except:
        return True
    if not comp1.isalpha():
        comp1 = ''
    if not comp2.isalpha():
        comp2 = ''
    comp1sum = 0
    comp2sum = 0
    for i in comp1:
        comp1sum += ord(i)
    for i in comp2:
        comp2sum += ord(i)
    if comp1sum == comp2sum:
        return True
    else:
        return False
