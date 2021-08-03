def scramble(s1, s2):
    for letter in 'abcdefghijklmnopqrstuwvxyz':
        if s1.count(letter) < s2.count(letter):
            return False
    return True


# def costam(s1,s2)
#    print s1
#    for letter in s2:
#        if letter in s1:
#            m = s1.index(letter)
#            s1 = s1[:m]+s1[m+1:]
#        else: return False
#    return True
