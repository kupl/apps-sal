def same_encryption(s1, s2):
    return s1[0] == s2[0] and s1[-1] == s2[-1] and (len(s1) % 9 == len(s2) % 9)
