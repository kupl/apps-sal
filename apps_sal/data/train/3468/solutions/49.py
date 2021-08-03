def scramble(s1, s2):
    while(len(s2) > 0):
        if(s1.count(s2[0]) < s2.count(s2[0])):
            return False
        else:
            s2 = s2.replace(s2[0], '')
    return True
