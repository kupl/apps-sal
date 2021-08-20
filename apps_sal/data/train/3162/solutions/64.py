def compare(s1, s2):
    count_s1 = 0
    count_s2 = 0
    if s1 == None or not s1.isalpha() or len(s1) <= 0:
        s1 = ''
    if s2 == None or not s2.isalpha() or len(s2) <= 0:
        s2 = ''
    for item in s1:
        count_s1 += ord(item.upper())
    for item in s2:
        count_s2 += ord(item.upper())
    return count_s1 == count_s2
